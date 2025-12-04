import json
from database import get_connection

class Disciplina:
    def __init__(self, id, id_usuario, nome, color, horas=60, presencas=0, faltas=0, modulos=None, provas=None):
        self.id = id
        self.id_usuario = id_usuario
        self.nome = nome
        self.color = color
        self.horas = int(horas)
        self.presencas = int(presencas)
        self.faltas = int(faltas)
        self.modulos = modulos if modulos else [] 
        self.provas = provas if provas else []

    def to_dict(self):
        return {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'name': self.nome,
            'color': self.color,
            'horas': self.horas,
            'presencas': self.presencas,
            'faltas': self.faltas,
            'modules': self.modulos,
            'provas': self.provas
        }
    
    @classmethod
    def from_dict(cls, data):
        nome_disciplina = data.get('name') or data.get('nome')
        return cls(
            id=data['id'],
            id_usuario=data['id_usuario'],
            nome=nome_disciplina,
            color=data.get('color', '#3498db'),
            horas=data.get('horas', 60),
            presencas=data.get('presencas', 0),
            faltas=data.get('faltas', 0),
            modulos=data.get('modules', []),
            provas=data.get('provas', [])
        )

class DisciplinaModel:
    def __init__(self):
        pass

    def _row_to_obj(self, r):
        modulos_list = json.loads(r['modulos']) if r['modulos'] else []
        provas_list = json.loads(r['provas']) if r['provas'] else []
        
        return Disciplina(
            id=r['id'],
            id_usuario=r['id_usuario'],
            nome=r['nome'],
            color=r['color'],
            horas=r['horas'],
            presencas=r['presencas'],
            faltas=r['faltas'],
            modulos=modulos_list,
            provas=provas_list
        )

    def pegar_todas(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM disciplinas")
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_obj(r) for r in rows]

    def listar_por_usuario(self, id_usuario):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM disciplinas WHERE id_usuario = ?", (id_usuario,))
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_obj(r) for r in rows]

    def buscar_por_id(self, id_disciplina):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM disciplinas WHERE id = ?", (id_disciplina,))
        r = cursor.fetchone()
        conn.close()
        return self._row_to_obj(r) if r else None

    def adicionar(self, d):
        conn = get_connection()
        cursor = conn.cursor()
        modulos_json = json.dumps(d.modulos)
        provas_json = json.dumps(d.provas)
        
        cursor.execute('''
            INSERT INTO disciplinas (id, id_usuario, nome, color, horas, presencas, faltas, modulos, provas)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (d.id, d.id_usuario, d.nome, d.color, d.horas, d.presencas, d.faltas, modulos_json, provas_json))
        conn.commit()
        conn.close()
    
    def atualizar(self, d):
        conn = get_connection()
        cursor = conn.cursor()
        modulos_json = json.dumps(d.modulos)
        provas_json = json.dumps(d.provas)

        cursor.execute('''
            UPDATE disciplinas 
            SET nome=?, color=?, horas=?, presencas=?, faltas=?, modulos=?, provas=?
            WHERE id=?
        ''', (d.nome, d.color, d.horas, d.presencas, d.faltas, modulos_json, provas_json, d.id))
        conn.commit()
        conn.close()

    def remover(self, id_disciplina):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM disciplinas WHERE id=?", (id_disciplina,))
        conn.commit()
        conn.close()