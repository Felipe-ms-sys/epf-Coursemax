import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Disciplina:
    def __init__(self, id, id_usuario, nome, horas, num_provas, metodo_avaliacao, notas=None):
        self.id = id
        self.id_usuario = id_usuario
        self.nome = nome
        self.horas = int(horas)
        self.num_provas = int(num_provas)
        self.metodo_avaliacao = metodo_avaliacao
        self.faltas_permitidas = int(self.horas * 0.25)

        if notas:
            self.notas = notas
        else:
            self.notas = {f"P{i+1}": None for i in range(self.num_provas)}

    def to_dict(self):
        return {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'nome': self.nome,
            'horas': self.horas,
            'faltas_permitidas': self.faltas_permitidas,
            'num_provas': self.num_provas,
            'metodo_avaliacao': self.metodo_avaliacao,
            'notas': self.notas
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            id_usuario=data['id_usuario'],
            nome=data['nome'],
            horas=data['horas'],
            num_provas=data['num_provas'],
            metodo_avaliacao=data['metodo_avaliacao'],
            notas=data.get('notas')
        )

class DisciplinaModel:
    FILE_PATH = os.path.join(DATA_DIR, 'disciplinas.json')

    def __init__(self):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        self.disciplinas = self._carregar()

    def _carregar(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        try:
            with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Disciplina.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _salvar(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([d.to_dict() for d in self.disciplinas], f, indent=4, ensure_ascii=False)

    def pegar_todas(self):
        return self.disciplinas
        
    def get_by_user_id(self, id_usuario):
        return [d for d in self.disciplinas if d.id_usuario == id_usuario]

    def buscar_por_id(self, id_disciplina):
        return next((d for d in self.disciplinas if d.id == id_disciplina), None)

    def adicionar(self, disciplina):
        self.disciplinas.append(disciplina)
        self._salvar()

    def atualizar(self, disciplina_atualizada):
        for i, d in enumerate(self.disciplinas):
            if d.id == disciplina_atualizada.id:
                self.disciplinas[i] = disciplina_atualizada
                self._salvar()
                break
    
    def remover(self, id_disciplina):
        self.disciplinas = [d for d in self.disciplinas if d.id != id_disciplina]
        self._salvar()