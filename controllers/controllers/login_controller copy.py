from bottle import Bottle, request, response
from .base_controller import BaseController
from services.login_service import LoginService

class LoginController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.login_service = LoginService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/logout', method='GET', callback=self.logout)

    def login(self):
        if request.method == 'GET':
            return self.render('login')
        
        email = request.forms.get('email')
        password = request.forms.get('password')
        
        user = self.login_service.autenticar(email, password)
        
        if user:
            response.set_cookie("user_id", str(user.id), secret='sua-chave-secreta-aqui')
            self.redirect('/dashboard')
        else:
            return self.render('login', error="Email ou senha inválidos")

    def logout(self):
        response.delete_cookie("user_id")
        self.redirect('/login')

login_routes = Bottle()
login_controller = LoginController(login_routes)