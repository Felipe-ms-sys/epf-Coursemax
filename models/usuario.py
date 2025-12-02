import hashlib
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Usuario:
    def __init__(self, id, nome, email, cpf, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha = senha

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'cpf': self.cpf,
            'senha': self.senha
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            nome=data['nome'],
            email=data['email'],
            cpf=data['cpf'],
            senha=data.get('senha', '')
        )

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(stored_password, provided_password):
        return stored_password == hashlib.sha256(provided_password.encode()).hexdigest()

class UsuarioModel:
    FILE_PATH = os.path.join(DATA_DIR, 'usuarios.json')

    def __init__(self):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        self.usuarios = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        try:
            with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Usuario.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.usuarios], f, indent=4, ensure_ascii=False)

    def pegar_todos(self):
        return self.usuarios

    def buscar_por_id(self, id_usuario):
        return next((u for u in self.usuarios if u.id == id_usuario), None)

    def adicionar(self, usuario):
        self.usuarios.append(usuario)
        self._save()

    def atualizar(self, usuario_atualizado):
        for i, usuario in enumerate(self.usuarios):
            if usuario.id == usuario_atualizado.id:
                self.usuarios[i] = usuario_atualizado
                self._save()
                break

    def remover(self, id_usuario):
        self.usuarios = [u for u in self.usuarios if u.id != id_usuario]
        self._save()