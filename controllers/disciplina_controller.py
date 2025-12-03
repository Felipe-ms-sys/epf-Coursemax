import json
from bottle import Bottle, request, response
from .base_controller import BaseController
from services.disciplina_service import DisciplinaService
from services.user_service import UserService  

class DisciplinaController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.disciplina_service = DisciplinaService()
        self.user_service = UserService()
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

        usuario = self.user_service.user_model.get_by_id(int(user_id))
        nome_real = usuario.name if usuario else "Estudante"

        disciplinas_objs = self.disciplina_service.listar_por_usuario(int(user_id))
        disciplinas_dicts = [d.to_dict() for d in disciplinas_objs]

        return self.render('dashboard', 
                           disciplines_json=json.dumps(disciplinas_dicts), 
                           user_name=nome_real)

    def adicionar(self):
        user_id = request.get_cookie("user_id", secret='sua-chave-secreta-aqui')
        if not user_id:
            self.redirect('/login')
            return

        nome = request.forms.get('disciplineName')
        color = request.forms.get('disciplineColor')
        
        self.disciplina_service.criar_disciplina(
            id_usuario=int(user_id), 
            nome=nome, 
            color=color, 
            horas=60, 
            num_provas=2, 
            metodo='Padrao'
        )
        self.redirect('/dashboard')

    def remover(self, id):
        self.disciplina_service.remover(id)
        self.redirect('/dashboard')

disciplina_routes = Bottle()
disciplina_controller = DisciplinaController(disciplina_routes)