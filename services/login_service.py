from models.user import UserModel, User

class LoginService:
    def __init__(self):
        self.user_model = UserModel()

    def autenticar(self, email, senha):
        if not email or not senha:
            return None
            
        email_limpo = email.strip().lower()
        
        users = self.user_model.get_all()
        
        user = next((u for u in users if u.email.lower() == email_limpo), None)

        if user and User.verify_password(user.password, senha):
            return user
            
        return None