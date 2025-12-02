<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro - Adicionar Disciplinas</title>
    <style>
        :root {
            --primary-color: #1ABC9C;
            --primary-dark: #16a085;
            --secondary-color: #2C3E50;
            --bg-gradient: linear-gradient(135deg, var(--secondary-color) 0%, var(--primary-color) 100%);
            --text-dark: #2C3E50;
            --text-light: #7f8c8d;
            --white: #ffffff;
            --shadow: 0 10px 40px rgba(0,0,0,0.2);
            --radius: 12px;
            --danger: #ff4757;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: var(--bg-gradient);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .cadastro-container {
            background: var(--white);
            padding: 40px;
            border-radius: 20px;
            box-shadow: var(--shadow);
            width: 100%;
            max-width: 600px;
            animation: slideUp 0.5s ease;
        }

        @keyframes slideUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h1 { text-align: center; color: var(--text-dark); margin-bottom: 5px; font-size: 26px; }
        .subtitle { text-align: center; color: var(--text-light); margin-bottom: 30px; font-size: 14px; }

        .progress-bar { display: flex; justify-content: center; gap: 10px; margin-bottom: 30px; position: relative;}
        .step { width: 35px; height: 35px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; position: relative; z-index: 1; font-size: 14px;}
        
        .step-done { background: var(--primary-color); color: white; cursor: pointer;}
        .step-active { background: var(--secondary-color); color: white; box-shadow: 0 0 0 4px rgba(44, 62, 80, 0.2); }

        .section-title { font-size: 18px; color: var(--text-dark); margin-bottom: 15px; font-weight: 600; display: flex; align-items: center; gap: 8px;}

        .add-discipline-form { display: flex; gap: 10px; margin-bottom: 20px; }
        
        .add-discipline-form input[type="text"] {
            flex: 1; padding: 12px 15px; border: 2px solid #e0e0e0;
            border-radius: var(--radius); font-size: 15px; transition: all 0.3s;
        }
        .add-discipline-form input:focus { outline: none; border-color: var(--primary-color); }

        .color-picker {
            width: 50px; height: 46px; border: 2px solid #e0e0e0;
            border-radius: var(--radius); cursor: pointer; padding: 2px;
        }

        .btn-add-disc {
            padding: 0 20px; background: var(--primary-color); color: white;
            border: none; border-radius: var(--radius); cursor: pointer;
            font-weight: 600; font-size: 20px; transition: all 0.3s;
        }
        .btn-add-disc:hover { background: var(--primary-dark); }

        .disciplines-list {
            max-height: 250px; overflow-y: auto; margin-bottom: 25px;
            border: 1px solid #eee; border-radius: var(--radius); padding: 10px;
        }

        .discipline-item {
            display: flex; align-items: center; justify-content: space-between;
            padding: 12px; background: #f8f9fa; border-radius: 8px; margin-bottom: 8px;
            animation: fadeIn 0.3s;
        }
        @keyframes fadeIn { from{opacity:0; transform: translateX(-10px)} to{opacity:1; transform: translateX(0)} }

        .discipline-info { display: flex; align-items: center; gap: 15px; }
        
        .discipline-color-badge {
            width: 20px; height: 20px; border-radius: 50%; border: 2px solid white; box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .btn-remove {
            padding: 6px 12px; background: #fff; color: var(--danger); border: 1px solid var(--danger);
            border-radius: 6px; cursor: pointer; font-size: 12px; font-weight: 600; transition: 0.2s;
        }
        .btn-remove:hover { background: var(--danger); color: white; }

        .empty-state { text-align: center; color: #95a5a6; padding: 30px 20px; }

        .btn-finish {
            width: 100%; padding: 14px; background: linear-gradient(135deg, var(--secondary-color), var(--primary-color));
            color: white; border: none; border-radius: var(--radius); font-size: 16px; font-weight: 600;
            cursor: pointer; transition: all 0.3s;
        }
        .btn-finish:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(26, 188, 156, 0.3); }
        .btn-finish:disabled { background: #ccc; cursor: not-allowed; transform: none; box-shadow: none; }

        .back-link { text-align: center; margin-top: 20px; font-size: 14px; }
        .back-link a { color: var(--text-light); text-decoration: none; transition: 0.2s; }
        .back-link a:hover { color: var(--primary-color); }

    </style>
</head>
<body>
    <div class="cadastro-container">
        <div style="text-align: center; margin-bottom: 20px;">
            <svg style="width: 60px; height: 60px;" viewBox="0 0 200 200">
                <circle cx="100" cy="100" r="90" fill="#2C3E50"/>
                <path d="M 65 105 L 95 135 L 145 75" fill="none" stroke="#1ABC9C" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        </div>

        <h1>Configurar Matérias</h1>
        <p class="subtitle">Passo 2 de 2 - O que você está estudando?</p>

        <div class="progress-bar">
            <div class="step step-done" onclick="goBack()">✓</div>
            <div class="step step-active">2</div>
        </div>

        <h3 class="section-title">📚 Adicionar Disciplina</h3>

        <div class="add-discipline-form">
            <input type="text" id="disciplineName" placeholder="Ex: Cálculo I, História...">
            <input type="color" id="disciplineColor" class="color-picker" value="#3498db">
            <button class="btn-add-disc" onclick="addDiscipline()">+</button>
        </div>

        <div class="disciplines-list" id="disciplinesList">
            <div class="empty-state">
                <p>Nenhuma matéria adicionada.</p>
            </div>
        </div>

        <button class="btn-finish" id="btnFinish" onclick="finishRegistration()" disabled>
            Finalizar Cadastro 🎉
        </button>

        <div class="back-link">
            <a href="#" onclick="goBack()">← Voltar para dados pessoais</a>
        </div>
    </div>

    <script>
        let disciplines = [];
        let nextId = 1;

        window.onload = function() {
            const tempUser = localStorage.getItem('tempUserData');
            if (!tempUser) {
                alert('Por favor, preencha seus dados primeiro.');
                window.location.href = 'cadastro_step1.html';
            }
        }

        function addDiscipline() {
            const nameInput = document.getElementById('disciplineName');
            const colorInput = document.getElementById('disciplineColor');
            const name = nameInput.value.trim();
            
            if (!name) return alert('Digite o nome da disciplina!');

            disciplines.push({
                id: nextId++,
                name: name,
                color: colorInput.value,
                modules: [],
                presences: 0,
                absences: 0,
                totalClasses: 40
            });
            
            nameInput.value = '';
            colorInput.value = '#' + Math.floor(Math.random()*16777215).toString(16);
            
            renderDisciplines();
            updateFinishButton();
        }

        function removeDiscipline(id) {
            disciplines = disciplines.filter(d => d.id !== id);
            renderDisciplines();
            updateFinishButton();
        }

        function renderDisciplines() {
            const list = document.getElementById('disciplinesList');
            
            if (disciplines.length === 0) {
                list.innerHTML = `<div class="empty-state"><p>Nenhuma matéria adicionada.</p></div>`;
                return;
            }

            list.innerHTML = '';
            disciplines.forEach(disc => {
                list.innerHTML += `
                    <div class="discipline-item">
                        <div class="discipline-info">
                            <div class="discipline-color-badge" style="background: ${disc.color}"></div>
                            <span style="font-weight:500; color:#333">${disc.name}</span>
                        </div>
                        <button class="btn-remove" onclick="removeDiscipline(${disc.id})">Remover</button>
                    </div>
                `;
            });
        }

        function updateFinishButton() {
            document.getElementById('btnFinish').disabled = disciplines.length === 0;
        }

        function finishRegistration() {
            const userData = JSON.parse(localStorage.getItem('tempUserData'));
            
            localStorage.setItem('userName', userData.name);
            localStorage.setItem('userEmail', userData.email);
            
            localStorage.setItem('disciplines', JSON.stringify(disciplines));

            localStorage.removeItem('tempUserData');

            alert('Cadastro realizado com sucesso!');
            window.location.href = 'student_dashboard.html';
        }

        function goBack() {
            window.location.href = 'cadastro_step1.html';
        }

        document.getElementById('disciplineName').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') addDiscipline();
        });
    </script>
</body>
</html>