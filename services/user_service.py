from bottle import request
from models.user import UserModel, User

class UserService:
    def __init__(self):
        self.user_model = UserModel()

    def get_all(self):
        return self.user_model.get_all()

    def save(self):
        name = request.forms.get('name')
        email = request.forms.get('email')
        cpf = request.forms.get('cpf')
        password = request.forms.get('password')

        if not name:
             raise ValueError("Nome é obrigatório")

        if not password:
            raise ValueError("Senha é obrigatória")

        if not User.validate_email(email):
            raise ValueError(f"Email inválido. Domínios permitidos: {', '.join(User.DOMINIOS_EMAIL)}")

        if not User.validate_cpf(cpf):
            raise ValueError("CPF inválido (deve conter 11 dígitos numéricos)")

        users = self.user_model.get_all()

        if any(u.email == email for u in users):
            raise ValueError("Email já cadastrado")

        last_id = max([u.id for u in users], default=0) if users else 0
        new_id = last_id + 1

        hashed_password = User.hash_password(password)
        user = User(id=new_id, name=name, email=email, cpf=cpf, password=hashed_password)
        self.user_model.add_user(user)
        return user

    def authenticate(self, email, password):
        if not email or not password:
            return None
            
        users = self.user_model.get_all()
        user = next((u for u in users if u.email == email), None)

        if user and User.verify_password(user.password, password):
            return user
        return None
        
    def get_by_id(self, user_id):
        return self.user_model.get_by_id(user_id)

    def edit_user(self, user):
        name = request.forms.get('name')
        email = request.forms.get('email')
        cpf = request.forms.get('cpf')

        user.name = name
        user.email = email
        user.cpf = cpf

        self.user_model.update_user(user)

    def delete_user(self, user_id):
        self.user_model.delete_user(user_id)