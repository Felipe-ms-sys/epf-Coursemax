from bottle import Bottle, request, response
from .base_controller import BaseController
from services.disciplina_service import DisciplinaService

class DisciplinaController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.disciplina_service = DisciplinaService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/dashboard', method='GET', callback=self.dashboard)
        self.app.route('/disciplinas/adicionar', method='POST', callback=self.adicionar)
        self.app.route('/disciplinas/remover/<id:int>', method='POST', callback=self.remover)

    def dashboard(self):
        user_id = request.get_cookie("user_id", secret='sua-chave-secreta-aqui')
        if not user_id:
            self.redirect('/login')
            return
            
        disciplinas = self.disciplina_service.listar_por_usuario(int(user_id))
        
        return self.render('dashboard', disciplines=disciplinas, user_name="Estudante")

    def adicionar(self):
        user_id = request.get_cookie("user_id", secret='sua-chave-secreta-aqui')
        if not user_id:
            self.redirect('/login')
        
        nome = request.forms.get('disciplineName')
        self.disciplina_service.criar_disciplina(int(user_id), nome, horas=60, num_provas=2, metodo='Padrao')
        
        self.redirect('/dashboard')

    def remover(self, id):
        self.disciplina_service.remover(id)
        self.redirect('/dashboard')

disciplina_routes = Bottle()
disciplina_controller = DisciplinaController(disciplina_routes)