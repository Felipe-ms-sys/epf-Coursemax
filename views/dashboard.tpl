<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painel de Estudos</title>
    <style>
        :root {
            --primary-color: #1ABC9C;
            --primary-dark: #16a085;
            --secondary-color: #2C3E50;
            --bg-gradient: linear-gradient(135deg, var(--secondary-color) 0%, var(--primary-color) 100%);
            --danger: #ff4757;
            --success: #2ecc71;
            --warning: #f1c40f;
            --text-dark: #2C3E50;
            --grey-light: #f8f9fa;
            --radius: 12px;
            --shadow-card: 0 4px 6px rgba(0,0,0,0.05);
            --shadow-hover: 0 10px 20px rgba(0,0,0,0.1);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: var(--bg-gradient);
            min-height: 100vh;
            padding: 20px;
            color: #333;
            overflow-y: scroll; 
        }

        .container { max-width: 1200px; margin: 0 auto; }

        .header {
            background: rgba(255, 255, 255, 0.95);
            padding: 15px 30px;
            border-radius: var(--radius);
            margin-bottom: 30px;
            box-shadow: var(--shadow-card);
            display: flex;
            justify-content: space-between;
            align-items: center;
            backdrop-filter: blur(10px);
        }

        .logo-area svg { width: 40px; height: 40px; }

        .user-info { display: flex; align-items: center; gap: 15px; }

        .user-avatar {
            width: 45px; height: 45px;
            border-radius: 50%;
            background: var(--secondary-color);
            color: white;
            display: flex; align-items: center; justify-content: center;
            font-weight: bold; font-size: 18px;
            border: 2px solid var(--primary-color);
        }

        .btn-logout {
            padding: 8px 16px;
            background: #fff;
            color: var(--danger);
            border: 1px solid var(--danger);
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.2s;
        }

        .btn-logout:hover { background: var(--danger); color: white; }

        .disciplines-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 25px;
        }

        .discipline-card {
            background: white;
            padding: 25px;
            border-radius: 16px;
            box-shadow: var(--shadow-card);
            cursor: pointer;
            transition: all 0.3s ease;
            border: 1px solid rgba(0,0,0,0.05);
            position: relative;
            overflow: hidden;
        }

        .discipline-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-hover);
            border-color: var(--primary-color);
        }

        .card-top-bar {
            position: absolute; top: 0; left: 0; width: 100%; height: 6px;
        }

        .discipline-header {
            display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;
        }

        .discipline-name { font-size: 22px; font-weight: 700; color: var(--text-dark); }
        
        .info-row {
            display: flex; justify-content: space-between;
            margin-bottom: 12px; font-size: 14px; color: #666;
        }

        .progress-container {
            margin-top: 15px;
        }
        .progress-label { display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 5px; }
        
        .progress-bar {
            width: 100%; height: 8px; background: #eee; border-radius: 10px; overflow: hidden;
        }
        .progress-fill { height: 100%; border-radius: 10px; transition: width 0.5s ease; }

        .badge { padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: bold; }
        .badge-good { background: #d4edda; color: #155724; }
        .badge-warning { background: #fff3cd; color: #856404; }
        .badge-danger { background: #f8d7da; color: #721c24; }

        .modal {
            display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(44, 62, 80, 0.8);
            z-index: 1000; align-items: center; justify-content: center;
            opacity: 0; transition: opacity 0.3s;
        }

        .modal.active { display: flex; opacity: 1; }

        .modal-content {
            background: white; width: 90%; max-width: 700px;
            border-radius: 20px; padding: 30px;
            max-height: 85vh; overflow-y: auto;
            position: relative;
            box-shadow: 0 20px 50px rgba(0,0,0,0.3);
            animation: modalPop 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        @keyframes modalPop {
            from { transform: scale(0.8); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }

        .modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 1px solid #eee; padding-bottom: 15px; }
        .close-btn { background: none; border: none; font-size: 28px; cursor: pointer; color: #999; }
        .close-btn:hover { color: var(--danger); }

        .tabs { display: flex; gap: 10px; margin-bottom: 20px; background: #f1f2f6; padding: 5px; border-radius: 10px; }
        .tab {
            flex: 1; padding: 10px; border: none; background: none;
            cursor: pointer; border-radius: 8px; font-weight: 600; color: #666; transition: all 0.2s;
        }
        .tab.active { background: white; color: var(--primary-color); box-shadow: 0 2px 5px rgba(0,0,0,0.05); }

        .tab-content { display: none; }
        .tab-content.active { display: block; animation: fadeIn 0.3s; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

        .module-item {
            background: var(--grey-light); padding: 15px; border-radius: 10px;
            margin-bottom: 10px; display: flex; align-items: center; gap: 15px;
            transition: background 0.2s;
        }
        .module-item:hover { background: #eef2f7; }
        
        input[type="checkbox"] { width: 20px; height: 20px; accent-color: var(--primary-color); cursor: pointer; }
        
        .module-text { flex: 1; font-size: 16px; transition: color 0.2s; }
        .module-text.completed { text-decoration: line-through; color: #aaa; }

        .btn-icon { background: none; border: none; cursor: pointer; opacity: 0.6; transition: opacity 0.2s; font-size: 18px; }
        .btn-icon:hover { opacity: 1; color: var(--danger); }

        .add-form { display: flex; gap: 10px; margin-top: 20px; }
        .add-form input { padding: 12px; border: 2px solid #eee; border-radius: 8px; flex: 1; }
        .add-form input:focus { border-color: var(--primary-color); outline: none; }
        
        .btn-primary {
            background: var(--primary-color); color: white; border: none; padding: 0 25px;
            border-radius: 8px; font-weight: bold; cursor: pointer;
        }
        .btn-primary:hover { background: var(--primary-dark); }

        .freq-stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); gap: 15px; margin-bottom: 20px; }
        .stat-box { background: var(--grey-light); padding: 15px; border-radius: 10px; text-align: center; }
        .stat-num { font-size: 24px; font-weight: 800; color: var(--secondary-color); }
        .stat-desc { font-size: 12px; color: #777; margin-top: 5px; text-transform: uppercase; letter-spacing: 1px; }

        .freq-actions { display: flex; gap: 10px; }
        .btn-action { flex: 1; padding: 15px; border: none; border-radius: 8px; color: white; font-weight: bold; cursor: pointer; font-size: 16px; display: flex; align-items: center; justify-content: center; gap: 8px; transition: transform 0.1s; }
        .btn-action:active { transform: scale(0.98); }
        .btn-present { background: var(--success); }
        .btn-absent { background: var(--danger); }

    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <div class="logo-area">
            <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" style="width:50px; height:50px">
                <circle cx="100" cy="100" r="90" fill="#2C3E50"/>
                <circle cx="100" cy="100" r="85" fill="none" stroke="#1ABC9C" stroke-width="4"/>
                <path d="M 65 105 L 95 135 L 145 75" fill="none" stroke="#1ABC9C" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        </div>
        
        <div class="user-info">
            <span style="font-weight: 600; color: #2C3E50;">Olá, <span id="userNameDisplay">Estudante</span></span>
            <div class="user-avatar" id="userAvatarDisplay">E</div>
            <button class="btn-logout" onclick="logout()">Sair</button>
        </div>
    </div>

    <div class="disciplines-grid" id="grid"></div>
</div>

<div class="modal" id="detailsModal">
    <div class="modal-content">
        <div class="modal-header">
            <h2 id="modalTitle" style="color: var(--secondary-color);">Título da Matéria</h2>
            <button class="close-btn" onclick="closeModal()">×</button>
        </div>

        <div class="tabs">
            <button class="tab active" onclick="setTab('content')">Conteúdos</button>
            <button class="tab" onclick="setTab('frequency')">Frequência</button>
        </div>

        <div id="tab-content" class="tab-content active">
            <div id="modulesList"></div>
            
            <form class="add-form" onsubmit="addModule(event)">
                <input type="text" id="newModuleInput" placeholder="Novo tópico ou assunto..." required>
                <button type="submit" class="btn-primary">Adicionar</button>
            </form>
        </div>

        <div id="tab-frequency" class="tab-content">
            <div class="freq-stats">
                <div class="stat-box">
                    <div class="stat-num" id="totalClasses">0</div>
                    <div class="stat-desc">Aulas Totais</div>
                </div>
                <div class="stat-box">
                    <div class="stat-num" style="color: var(--success)" id="presentCount">0</div>
                    <div class="stat-desc">Presenças</div>
                </div>
                <div class="stat-box">
                    <div class="stat-num" style="color: var(--danger)" id="absentCount">0</div>
                    <div class="stat-desc">Faltas</div>
                </div>
                <div class="stat-box">
                    <div class="stat-num" id="percentage">0%</div>
                    <div class="stat-desc">Frequência</div>
                </div>
            </div>

            <div id="frequencyMessage" style="margin-bottom: 20px; padding: 10px; border-radius: 8px; font-size: 14px; text-align: center;"></div>

            <div class="freq-actions">
                <button class="btn-action btn-present" onclick="addAttendance(true)">
                    <span>✓</span> Presente
                </button>
                <button class="btn-action btn-absent" onclick="addAttendance(false)">
                    <span>✕</span> Faltei
                </button>
            </div>
            
            <div style="margin-top: 20px; text-align: center;">
                <small style="color: #999">Total de aulas previstas: <input type="number" id="editTotalClasses" style="width: 60px; padding: 5px;" onchange="updateTotalConfig()"></small>
            </div>
        </div>
    </div>
</div>

<script>
    let disciplines = JSON.parse(localStorage.getItem('disciplines')) || [
        { id: 1, name: 'Matemática', color: '#3498db', totalClasses: 40, presences: 30, absences: 2, modules: [{id: 1, text: 'Funções', done: true}, {id: 2, text: 'Logaritmos', done: false}] },
        { id: 2, name: 'Física', color: '#e74c3c', totalClasses: 40, presences: 35, absences: 0, modules: [{id: 3, text: 'Cinemática', done: false}] },
        { id: 3, name: 'Química', color: '#9b59b6', totalClasses: 30, presences: 28, absences: 1, modules: [] }
    ];

    let currentId = null;

    window.onload = function() {
        const user = localStorage.getItem('userName') || 'Visitante';
        document.getElementById('userNameDisplay').textContent = user;
        document.getElementById('userAvatarDisplay').textContent = user.charAt(0);
        renderGrid();
    };

    function save() {
        localStorage.setItem('disciplines', JSON.stringify(disciplines));
        renderGrid();
        if(currentId) updateModalStats();
    }

    function renderGrid() {
        const grid = document.getElementById('grid');
        grid.innerHTML = '';

        disciplines.forEach(d => {
            const completedModules = d.modules.filter(m => m.done).length;
            const progress = d.modules.length ? (completedModules / d.modules.length) * 100 : 0;
            const freq = d.totalClasses ? (d.presences / d.totalClasses) * 100 : 100;

            let badgeClass = 'badge-good';
            if(freq < 75) badgeClass = 'badge-danger';
            else if(freq < 85) badgeClass = 'badge-warning';

            grid.innerHTML += `
                <div class="discipline-card" onclick="openModal(${d.id})">
                    <div class="card-top-bar" style="background: ${d.color}"></div>
                    <div class="discipline-header">
                        <span class="discipline-name">${d.name}</span>
                        <span class="badge ${badgeClass}">${freq.toFixed(0)}% Freq.</span>
                    </div>
                    
                    <div class="info-row">
                        <span>Aulas Presenciais:</span>
                        <strong>${d.presences}/${d.totalClasses}</strong>
                    </div>
                    
                    <div class="progress-container">
                        <div class="progress-label">
                            <span>Progresso do Conteúdo</span>
                            <span>${progress.toFixed(0)}%</span>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: ${progress}%; background: ${d.color}"></div>
                        </div>
                    </div>
                </div>
            `;
        });
    }

    function openModal(id) {
        currentId = id;
        const data = disciplines.find(d => d.id === id);
        
        document.getElementById('modalTitle').textContent = data.name;
        document.getElementById('modalTitle').style.color = data.color;
        
        renderModuleList(data);
        
        updateModalStats();
        
        document.getElementById('detailsModal').classList.add('active');
    }

    function closeModal() {
        document.getElementById('detailsModal').classList.remove('active');
        currentId = null;
    }

    function setTab(tabName) {
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        event.target.classList.add('active');
        
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
        document.getElementById(`tab-${tabName}`).classList.add('active');
    }

    function renderModuleList(data) {
        const list = document.getElementById('modulesList');
        list.innerHTML = '';
        
        if(data.modules.length === 0) {
            list.innerHTML = '<p style="text-align:center; color:#999; margin: 20px 0;">Nenhum conteúdo cadastrado.</p>';
            return;
        }

        data.modules.forEach(m => {
            list.innerHTML += `
                <div class="module-item">
                    <input type="checkbox" ${m.done ? 'checked' : ''} onchange="toggleModule(${m.id})">
                    <span class="module-text ${m.done ? 'completed' : ''}">${m.text}</span>
                    <button class="btn-icon" onclick="deleteModule(${m.id})">🗑️</button>
                </div>
            `;
        });
    }

    function addModule(e) {
        e.preventDefault();
        const input = document.getElementById('newModuleInput');
        if(!input.value) return;

        const disc = disciplines.find(d => d.id === currentId);
        disc.modules.push({
            id: Date.now(),
            text: input.value,
            done: false
        });
        
        input.value = '';
        save();
        renderModuleList(disc);
    }

    function toggleModule(modId) {
        const disc = disciplines.find(d => d.id === currentId);
        const mod = disc.modules.find(m => m.id === modId);
        mod.done = !mod.done;
        save();
        renderModuleList(disc);
    }

    function deleteModule(modId) {
        if(confirm('Excluir este item?')) {
            const disc = disciplines.find(d => d.id === currentId);
            disc.modules = disc.modules.filter(m => m.id !== modId);
            save();
            renderModuleList(disc);
        }
    }

    function updateModalStats() {
        const disc = disciplines.find(d => d.id === currentId);
        
        document.getElementById('totalClasses').textContent = disc.totalClasses;
        document.getElementById('presentCount').textContent = disc.presences;
        document.getElementById('absentCount').textContent = disc.absences;
        document.getElementById('editTotalClasses').value = disc.totalClasses;

        const freq = (disc.presences / disc.totalClasses) * 100;
        document.getElementById('percentage').textContent = freq.toFixed(1) + '%';
        
        const msgDiv = document.getElementById('frequencyMessage');
        if(freq < 75) {
            msgDiv.style.background = '#f8d7da';
            msgDiv.style.color = '#721c24';
            msgDiv.innerHTML = `⚠️ <strong>Cuidado!</strong> Você precisa de mais presenças para atingir 75%.`;
        } else {
            msgDiv.style.background = '#d4edda';
            msgDiv.style.color = '#155724';
            msgDiv.innerHTML = `✅ <strong>Muito bem!</strong> Frequência segura.`;
        }
    }

    function addAttendance(isPresent) {
        const disc = disciplines.find(d => d.id === currentId);
        
        if(disc.presences + disc.absences >= disc.totalClasses) {
            alert('Você atingiu o limite de aulas cadastradas para esta matéria. Aumente o "Total de aulas previstas" abaixo.');
            return;
        }

        if(isPresent) disc.presences++;
        else disc.absences++;
        
        save();
    }

    function updateTotalConfig() {
        const val = parseInt(document.getElementById('editTotalClasses').value);
        if(val > 0) {
            const disc = disciplines.find(d => d.id === currentId);
            disc.totalClasses = val;
            save();
        }
    }

    function logout() {
        localStorage.removeItem('userEmail');
        window.location.href = 'login_screen_updated.html';
    }
</script>

</body>
</html>