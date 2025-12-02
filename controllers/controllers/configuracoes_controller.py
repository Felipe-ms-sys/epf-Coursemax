from bottle import Bottle, request, response
from .base_controller import BaseController
from services.configuracoes_service import ConfiguracaoService

class ConfiguracoesController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.config_service = ConfiguracaoService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/configuracoes/excluir', method='POST', callback=self.excluir_conta)

    def excluir_conta(self):
        user_id = request.get_cookie("user_id", secret='sua-chave-secreta-aqui')
        if user_id:
            self.config_service.excluir_usuario(int(user_id))
            response.delete_cookie("user_id")
        self.redirect('/login')

configuracoes_routes = Bottle()
configuracoes_controller = ConfiguracoesController(configuracoes_routes)