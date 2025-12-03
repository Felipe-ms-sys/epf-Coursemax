import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Disciplina:
    def __init__(self, id, id_usuario, nome, color, horas=60, presencas=0, faltas=0, modulos=None):
        self.id = id
        self.id_usuario = id_usuario
        self.nome = nome
        self.color = color
        self.horas = int(horas)
        self.presencas = int(presencas)
        self.faltas = int(faltas)
        self.modulos = modulos if modulos else [] 

    def to_dict(self):
        return {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'nome': self.nome,
            'color': self.color,
            'horas': self.horas,
            'presencas': self.presencas,
            'faltas': self.faltas,
            'modules': self.modulos 
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            id_usuario=data['id_usuario'],
            nome=data['nome'],
            color=data.get('color', '#3498db'),
            horas=data.get('horas', 60),
            presencas=data.get('presencas', 0),
            faltas=data.get('faltas', 0),
            modulos=data.get('modules', [])
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

    def listar_por_usuario(self, id_usuario):
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