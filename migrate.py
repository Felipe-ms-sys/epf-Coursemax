import json
import os
import sqlite3
from models.user import UserModel, User
from models.disciplina import DisciplinaModel, Disciplina

USERS_JSON = os.path.join('data', 'users.json')
DISC_JSON = os.path.join('data', 'disciplinas.json')

def migrar():
    print("🚀 Iniciando migração dos dados...")
    
    if os.path.exists(USERS_JSON):
        with open(USERS_JSON, 'r', encoding='utf-8') as f:
            try:
                users_data = json.load(f) 
                u_model = UserModel()     
                
                count = 0
                for item in users_data:
                    u = User.from_dict(item)
                    
                    if not u_model.get_by_id(u.id):
                        u_model.add_user(u) 
                        count += 1
                print(f"✅ {count} usuários transferidos com sucesso.")
            except json.JSONDecodeError:
                print("⚠️  O arquivo users.json estava vazio ou inválido.")
    else:
        print("⚠️  Arquivo users.json não encontrado (nenhum usuário para migrar).")

    if os.path.exists(DISC_JSON):
        with open(DISC_JSON, 'r', encoding='utf-8') as f:
            try:
                disc_data = json.load(f)  
                d_model = DisciplinaModel() 
                
                count = 0
                for item in disc_data:
                    d = Disciplina.from_dict(item)
                    
                    if not d_model.buscar_por_id(d.id):
                        d_model.adicionar(d)
                        count += 1
                print(f"✅ {count} disciplinas transferidas com sucesso.")
            except json.JSONDecodeError:
                print("⚠️  O arquivo disciplinas.json estava vazio ou inválido.")
    else:
        print("⚠️  Arquivo disciplinas.json não encontrado.")
        
    print("\n🏁 Migração concluída! O arquivo 'coursemax.db' agora contém seus dados.")

if __name__ == "__main__":
    migrar()