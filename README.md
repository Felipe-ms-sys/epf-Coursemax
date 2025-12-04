# 📈CourseMax: Sistema de gerenciamento acadêmico pessoal

Este projeto foi desenvolvido como parte do projeto final da disciplina de Programação Orientada a Objetos. A aplicação segue uma arquitetura organizada em camadas (Models, Services, Controllers e Views) e utiliza o framework Bottle com JSON como banco de dados principal.

A proposta deste projeto consistiu na criação de um sistema que facilite a organização acadêmica pessoal do usuário, permitindo-lhe reunir informações relacionadas à frequência, aos módulos disciplinares e às notas de provas.

---

## Membros da equipe:
* **Felipe Melo de Sousa** - 2420215370 
* **Gabriel Portacio Candeia Costa** - 242015488

---

## 💡 Objetivo

Fornecer uma base simples, extensível e didática para construção de aplicações web orientadas a objetos com aplicações WEB em Python, ideal para trabalhos finais ou exercícios práticos.

---

## 🗂 Estrutura de Pastas

```bash
CourseMax/
├── app.py # Configuração principal e inicialização do Bottle
├── main.py # Ponto de entrada da aplicação
├── config.py # Configurações globais (banco, paths, chaves)
├── requirements.txt # Dependências
├── Makefile 
│
├── data/  
│   ├── disciplinas.json # Armazenamento de disciplinas/módulos/notas
│   └── users.json # Armazenamento de usuários cadastrados
│
├── models/
│   ├── disciplina.py # Classes Disciplina e DisciplinaModel
│   └── user.py # Classes User e UserModel
│
├── services/
│   ├── cadastro_service.py # Validação de informações e criação de conta
│   ├── disciplina_service.py   # Cria e manipula matérias
│   ├── login_service.py        # Verificação de credenciais
│   ├── study_service.py        # (Auxiliar) Serviços de estudo
│   └── user_service.py         # Lógica CRUD para usuários
│
├── controllers/ # Camada de Controle (Rotas e requisições HTTP)
│   ├── __init__.py
│   ├── base_controller.py
│   ├── cadastro_controller.py
│   ├── disciplina_controller.py
│   ├── login_controller.py
│   ├── study_controller.py
│   └── user_controller.py
│
├── views/
│   ├── cadastro_step1.tpl
│   ├── cadastro_step2.tpl
│   ├── dashboard.tpl
│   ├── helper-final.tpl
│   ├── layout.tpl
│   ├── login.tpl
│   ├── user_form.tpl
│   └── users.tpl
│
└── static/
    ├── css/
    │   ├── helper.css
    │   └── style.css
    ├── img/
    │   ├── BottleLogo.png
    │   └── logo-new.jpg
    └── js/
        ├── helper.js
        └── main.js
```

---

## ⚙️ Funcionalidades

### Autenticação
* Login e logout
* Cadastro
* Hash de senhas com strings aleatórias
* Verificação de formato para cpf e de domínios para email

### Usuários
* CRUD de usuários 
* Persistência dos dados no banco JSON
* Exibição personalizada, nome e inicial no dashboard

### Disciplinas
* CRUD de disciplinas
* Persistência dos dados no banco JSON
* Controle de frequência, notas de avaliações e módulos disciplinares
* Personalização por cor e cards únicos
---

## 🔧 Execução

### 1. Clone o repositório

```bash
git clone https://github.com/Felipe-ms-sys/epf-Coursemax.git
cd epf-Coursemax
```
### 2. Crie um ambiente virtual
```bash
python -m venv venv
venv\\Scripts\\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac
```
### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação
```bash
python main.py
```

### 5. Abra o navegador
```bash
Acesse sua aplicação em http://localhost:8080
```

