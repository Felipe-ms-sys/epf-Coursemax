from bottle import Bottle, request
from .base_controller import BaseController
from services.cadastro_service import CadastroService

class CadastroController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.cadastro_service = CadastroService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/cadastro', method='GET', callback=self.step1)
        self.app.route('/cadastro/disciplinas', method='GET', callback=self.step2)
        self.app.route('/cadastro/finalizar', method='POST', callback=self.finalizar)

    def step1(self):
        return self.render('cadastro_step1')

    def step2(self):
        return self.render('cadastro_step2')

    def finalizar(self):
        
        nome = request.forms.get('name')
        email = request.forms.get('email')
        cpf = request.forms.get('cpf')
        senha = request.forms.get('password')
        
        try:
            self.cadastro_service.cadastrar_usuario(nome, email, cpf, senha)
            self.redirect('/login')
        except ValueError as e:
            return f"Erro no cadastro: {str(e)}"

cadastro_routes = Bottle()
cadastro_controller = CadastroController(cadastro_routes)