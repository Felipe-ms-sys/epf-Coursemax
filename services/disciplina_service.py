from models.disciplina import DisciplinaModel, Disciplina

class DisciplinaService:
    def __init__(self):
        self.disciplina_model = DisciplinaModel()

    def listar_por_usuario(self, id_usuario):
        return self.disciplina_model.listar_por_usuario(id_usuario)

    def criar_disciplina(self, id_usuario, nome, color, horas, num_provas, metodo):
        if not nome:
            raise ValueError("Nome da disciplina é obrigatório")

        todas = self.disciplina_model.pegar_todas()
        novo_id = max([d.id for d in todas], default=0) + 1

        nova_disciplina = Disciplina(
            id=novo_id,
            id_usuario=id_usuario,
            nome=nome,
            color=color,
            horas=horas,
            presencas=0,
            faltas=0,
            modulos=[]
        )
        
        self.disciplina_model.adicionar(nova_disciplina)
        return nova_disciplina
    
    def atualizar(self, dados_disciplina):
        disciplina = Disciplina.from_dict(dados_disciplina)
        self.disciplina_model.atualizar(disciplina)

    def remover(self, id_disciplina):
        self.disciplina_model.remover(id_disciplina)