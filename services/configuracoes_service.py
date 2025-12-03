from models.user import UserModel

class ConfiguracaoService:
    def __init__(self):
        self.user_model = UserModel()

    def editar_usuario(self, usuario_atualizado):
        usuario_existente = self.user_model.get_by_id(usuario_atualizado.id)
        if not usuario_existente:
            raise ValueError("Usuário não encontrado para edição")
        
        self.user_model.update_user(usuario_atualizado)
        return usuario_existente

    def excluir_usuario(self, id_usuario):
        usuario = self.user_model.get_by_id(id_usuario)
        if not usuario:
            raise ValueError("Usuário não encontrado para exclusão")

        self.user_model.delete_user(id_usuario)