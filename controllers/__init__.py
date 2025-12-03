from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.login_controller import login_routes
from controllers.disciplina_controller import disciplina_routes
from controllers.cadastro_controller import cadastro_routes


def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(login_routes)
    app.merge(disciplina_routes)
    app.merge(cadastro_routes)
    