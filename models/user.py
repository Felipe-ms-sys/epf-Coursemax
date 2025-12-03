import json
import os
import hashlib

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class User:
    DOMINIOS_EMAIL = ['gmail.com', 'hotmail.com', 'outlook.com', 'yahoo.com']

    def __init__(self, id, email, cpf, name=None, nome=None, password=None, senha=None, **kwargs):
        self.id = id
        self.email = email
        self.cpf = cpf
        self.name = name or nome
        self.password = password or senha

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.name,
            'email': self.email,
            'cpf': self.cpf,
            'senha': self.password
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data.get('name') or data.get('nome'),
            email=data['email'],
            cpf=data.get('cpf', ''),
            password=data.get('password') or data.get('senha')
        )
        
    @staticmethod
    def validate_email(email):
        if not email or '@' not in email:
            return False
        try:
            domain = email.split('@')[1]
            return domain in User.DOMINIOS_EMAIL
        except IndexError:
            return False

    @staticmethod
    def validate_cpf(cpf):
        return len(str(cpf)) == 11

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(stored_password, provided_password):
        return stored_password == hashlib.sha256(provided_password.encode()).hexdigest()


class UserModel:
    FILE_PATH = os.path.join(DATA_DIR, 'users.json')

    def __init__(self):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        self.users = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        try:
            with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [User.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.users

    def get_by_id(self, user_id):
        return next((u for u in self.users if u.id == user_id), None)

    def add_user(self, user):
        self.users.append(user)
        self._save()

    def update_user(self, updated_user):
        for i, user in enumerate(self.users):
            if user.id == updated_user.id:
                self.users[i] = updated_user
                self._save()
                break

    def delete_user(self, user_id):
        self.users = [u for u in self.users if u.id != user_id]
        self._save()