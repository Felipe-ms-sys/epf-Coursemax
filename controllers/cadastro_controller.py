from bottle import Bottle, request, response
from .base_controller import BaseController
from services.cadastro_service import CadastroService
from services.disciplina_service import DisciplinaService

class CadastroController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.cadastro_service = CadastroService()
        self.disciplina_service = DisciplinaService() 
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
        data = request.json
        if not data:
            response.status = 400
            return {'success': False, 'error': 'Nenhum dado recebido'}

        user_data = data.get('user')
        disciplines_data = data.get('disciplines')

        cpf_real = user_data.get('cpf')

        try:
            novo_usuario = self.cadastro_service.cadastrar_usuario(
                user_data['name'], 
                user_data['email'], 
                cpf_real, 
                user_data['pass']
            )
    
            for disc in disciplines_data:
                 self.disciplina_service.criar_disciplina(
                    id_usuario=novo_usuario.id, 
                    nome=disc['name'], 
                    color=disc.get('color', '#3498db'),
                    horas=60, 
                    num_provas=2, 
                    metodo='Padrao'
                 )
            
            response.set_cookie("user_id", str(novo_usuario.id), secret='sua-chave-secreta-aqui')
                 
            return {'success': True}

        except ValueError as e:
            return {'success': False, 'error': str(e)}
        except Exception as e:
            print(f"Erro Crítico: {e}")
            return {'success': False, 'error': "Erro interno no servidor"}

cadastro_routes = Bottle()
cadastro_controller = CadastroController(cadastro_routes)