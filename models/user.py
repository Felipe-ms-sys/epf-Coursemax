import json
import os
import hashlib

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class User:
    DOMINIOS_EMAIL = ['gmail.com', 'hotmail.com', 'outlook.com', 'yahoo.com']

    def __init__(self, id, name, email, cpf, password):
        self.id = id
        self.name = name
        self.email = email
        self.cpf = cpf
        self.password = password

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'cpf': self.cpf,
            'password': self.password
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            email=data['email'],
            cpf=data['cpf'],
            password=data.get('password', '')
        )


class UserModel:
    FILE_PATH = os.path.join(DATA_DIR, 'users.json')

    def __init__(self):
        self.users = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [User(**item) for item in data]

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