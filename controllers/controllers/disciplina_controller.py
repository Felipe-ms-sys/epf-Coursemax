import json
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
        user_id = request.get_cookie("user_id", secret='sua-chave-secreta-aqui') or 1
        
        disciplinas_objs = self.disciplina_service.listar_por_usuario(int(user_id))
        
        disciplinas_dicts = [d.to_dict() for d in disciplinas_objs]
        
        return self.render('dashboard', 
                           disciplines_json=json.dumps(disciplinas_dicts), 
                           user_name="Estudante")

    def adicionar(self):
        user_id = request.get_cookie("user_id", secret='sua-chave-secreta-aqui') or 1
        nome = request.forms.get('disciplineName')
        color = request.forms.get('disciplineColor')
        
        pass 

disciplina_routes = Bottle()
disciplina_controller = DisciplinaController(disciplina_routes)