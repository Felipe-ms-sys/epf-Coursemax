from models.user import UserModel, User

class CadastroService:
    DOMINIOS_PERMITIDOS = ['gmail.com', 'hotmail.com', 'outlook.com', 'unb.br']

    def __init__(self):
        self.user_model = UserModel()

    def _validar_email(self, email):
        if not email or '@' not in email:
            return False
        try:
            _, dominio = email.lower().split('@')
            return dominio in self.DOMINIOS_PERMITIDOS
        except ValueError:
            return False

    def _validar_cpf(self, cpf):
        if not cpf:
            return False
        cpf_limpo = str(cpf).replace('.', '').replace('-', '').strip()
        return len(cpf_limpo) == 11 and cpf_limpo.isdigit()

    def cadastrar_usuario(self, nome, email, cpf, senha):
        if not nome or not senha:
            raise ValueError("Nome e Senha são obrigatórios")
        
        email = email.strip().lower()

        if not self._validar_email(email):
            raise ValueError(f"Domínio de email inválido. Permitidos: {', '.join(self.DOMINIOS_PERMITIDOS)}")

        if not self._validar_cpf(cpf):
            raise ValueError("CPF deve conter 11 dígitos numéricos")

        users = self.user_model.get_all()
        if any(u.email.lower() == email for u in users):
            raise ValueError("Email já cadastrado")

        last_id = max([u.id for u in users], default=0) if users else 0
        new_id = last_id + 1
        
        senha_hash = User.hash_password(senha)
        
        novo_usuario = User(
            id=new_id, 
            name=nome, 
            email=email, 
            cpf=cpf, 
            password=senha_hash
        )
        
        self.user_model.add_user(novo_usuario)
        return novo_usuario