from models.usuario import UsuarioModel, Usuario

class LoginService:
    def __init__(self):
        self.usuario_model = UsuarioModel()

    def autenticar(self, email, senha):

        with open('data/usuarios.json', 'r', encoding='utf-8') as f:
            
            usuarios = self.usuario_model.pegar_todos()
            usuario = next((u for u in usuarios if u.email == email), None)

            if usuario and Usuario.verify_password(usuario.senha, senha):
                return usuario
            return None