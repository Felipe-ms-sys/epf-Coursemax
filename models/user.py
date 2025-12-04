import sqlite3
from database import get_connection

class User:
    DOMINIOS_EMAIL = ['gmail.com', 'hotmail.com', 'outlook.com', 'yahoo.com', 'unb.br']

    def __init__(self, id, email, cpf, name=None, nome=None, password=None, senha=None, **kwargs):
        self.id = id
        self.email = email
        self.cpf = cpf
        self.name = name or nome
        self.password = password or senha
        
    @staticmethod
    def validate_email(email):
        if not email or '@' not in email: return False
        try:
            return email.split('@')[1] in User.DOMINIOS_EMAIL
        except IndexError: return False

    @staticmethod
    def validate_cpf(cpf):
        return len(str(cpf)) == 11

    @staticmethod
    def hash_password(password):
        import hashlib, os
        salt = os.urandom(16).hex()
        hash_result = hashlib.sha256((salt + password).encode()).hexdigest()
        return f"{salt}${hash_result}"

    @staticmethod
    def verify_password(stored_password, provided_password):
        import hashlib
        try:
            salt, hash_armazenado = stored_password.split('$')
            return hashlib.sha256((salt + provided_password).encode()).hexdigest() == hash_armazenado
        except ValueError: return False

class UserModel:
    def __init__(self):
        pass

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        conn.close()
        
        return [User(id=r['id'], name=r['name'], email=r['email'], cpf=r['cpf'], password=r['password']) for r in rows]

    def get_by_id(self, user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        r = cursor.fetchone()
        conn.close()
        
        if r:
            return User(id=r['id'], name=r['name'], email=r['email'], cpf=r['cpf'], password=r['password'])
        return None

    def add_user(self, user):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (id, name, email, cpf, password) VALUES (?, ?, ?, ?, ?)",
                       (user.id, user.name, user.email, user.cpf, user.password))
        conn.commit()
        conn.close()

    def update_user(self, user):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name=?, email=?, cpf=? WHERE id=?",
                       (user.name, user.email, user.cpf, user.id))
        conn.commit()
        conn.close()

    def delete_user(self, user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()
        conn.close()