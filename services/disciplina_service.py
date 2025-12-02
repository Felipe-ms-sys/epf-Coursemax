from models.disciplina import DisciplinaModel, Disciplina

class DisciplinaService:
    def __init__(self):
        self.disciplina_model = DisciplinaModel()

    def listar_por_usuario(self, id_usuario):
        return self.disciplina_model.get_by_user_id(id_usuario)

    def criar_disciplina(self, id_usuario, nome, horas, num_provas, metodo):
        if not nome or not horas:
            raise ValueError("Dados obrigatórios faltando")

        try:
            horas = int(horas)
            num_provas = int(num_provas)
        except ValueError:
            raise ValueError("Horas e provas devem ser números")

        todas = self.disciplina_model.pegar_todas()
        novo_id = max([d.id for d in todas], default=0) + 1

        nova_disciplina = Disciplina(novo_id, id_usuario, nome, horas, num_provas, metodo)
        self.disciplina_model.adicionar(nova_disciplina)
        return nova_disciplina
    
    def buscar_por_id(self, id_disciplina):
        return self.disciplina_model.buscar_por_id(id_disciplina)
        
    def atualizar(self, disciplina):
        self.disciplina_model.atualizar(disciplina)

    def remover(self, id_disciplina):
        self.disciplina_model.remover(id_disciplina)