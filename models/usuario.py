import json
import os
import hashlib

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
            cpf=data.get('cpf', ''), 
            senha=data['senha']
        )
    
    @staticmethod
    def hash_password(password):
        """Criptografa a senha para não salvar texto puro"""
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(stored_password, provided_password):
        """Verifica se a senha digitada bate com a salva"""
        return stored_password == hashlib.sha256(provided_password.encode()).hexdigest()


class UsuarioModel:
    FILE_PATH = os.path.join(DATA_DIR, 'users.json')

    def __init__(self):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        self.usuarios = self._carregar()

    def _carregar(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        try:
            with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Usuario.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _salvar(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.usuarios], f, indent=4, ensure_ascii=False)

    def pegar_todos(self):
        return self.usuarios

    def adicionar(self, usuario):
        self.usuarios.append(usuario)
        self._salvar()

    def buscar_por_id(self, user_id):
        return next((u for u in self.usuarios if u.id == user_id), None)