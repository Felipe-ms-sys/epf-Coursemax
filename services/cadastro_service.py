from models.usuario 
import UsuarioModel, Usuario

class CadastroService:
    DOMINIOS_PERMITIDOS = ['gmail.com', 'hotmail.com', 'outlook.com', 'unb.br']

    def __init__(self):
        self.usuario_model = UsuarioModel()

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

        if not self._validar_email(email):
            raise ValueError(f"Domínio de e mail inválido")

        if not self._validar_cpf(cpf):
            raise ValueError("CPF deve conter 11 dígitos numéricos")

        usuarios = self.usuario_model.pegar_todos()
        if any(u.email == email for u in usuarios):
            raise ValueError("Email já cadastrado")

        novo_id = max([u.id for u in usuarios], default=0) + 1
        
        senha_hash = Usuario.hash_password(senha)
        
        novo_usuario = Usuario(novo_id, nome, email, cpf, senha_hash)
        self.usuario_model.adicionar(novo_usuario)
        return novo_usuario