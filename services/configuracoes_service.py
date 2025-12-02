from models.usuario import UsuarioModel

class ConfiguracaoService:
    def __init__(self):
        self.usuario_model = UsuarioModel()

    def editar_usuario(self, usuario_atualizado):
        usuario_existente = self.usuario_model.buscar_por_id(usuario_atualizado.id)
        if not usuario_existente:
            raise ValueError("Usuário não encontrado para edição")
        
        self.usuario_model.atualizar(usuario_atualizado)
        return usuario_existente

    def excluir_usuario(self, id_usuario):
        usuario = self.usuario_model.buscar_por_id(id_usuario)
        if not usuario:
            raise ValueError("Usuário não encontrado para exclusão")

        self.usuario_model.remover(id_usuario)