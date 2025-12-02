from bottle import route, view, request, redirect
from services.study_service import StudyService

service = StudyService()

@route('/dashboard')
@view('dashboard')
def dashboard():
    user_id = 1 
    
    disciplinas = service.get_disciplines(user_id)
    
    return dict(disciplines=disciplinas, user_name="Estudante")

@route('/cadastro/disciplinas')
@view('cadastro_step2')
def cadastro_disciplinas_view():
    return dict()

@route('/cadastro/disciplinas', method='POST')
def cadastro_disciplinas_logic():
    name = request.forms.get('disciplineName')
    color = request.forms.get('disciplineColor')
    
    service.add_discipline(name, color, 1)
    
    return redirect('/dashboard')