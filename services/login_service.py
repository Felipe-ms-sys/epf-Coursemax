from models.user import UserModel, User

class LoginService:
    def __init__(self):
        self.user_model = UserModel()

    def autenticar(self, email, senha):
        users = self.user_model.get_all()
        user = next((u for u in users if u.email == email), None)

        if user and User.verify_password(user.password, senha):
            return user
            
        return None