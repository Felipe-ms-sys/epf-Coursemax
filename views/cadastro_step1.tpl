<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro - Passo 1</title>
    <link rel="icon" type="image/jpg" href="/static/img/logo-new.jpg">
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

        .container {
            background: var(--white);
            padding: 40px;
            border-radius: 20px;
            box-shadow: var(--shadow);
            width: 100%;
            max-width: 500px;
            animation: slideUp 0.5s ease;
        }

        @keyframes slideUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h1 { text-align: center; color: var(--text-dark); margin-bottom: 5px; }
        .subtitle { text-align: center; color: var(--text-light); margin-bottom: 25px; font-size: 14px; }

        .progress-bar { display: flex; justify-content: center; gap: 10px; margin-bottom: 30px; }
        .step { width: 35px; height: 35px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; position: relative; z-index: 1; }
        
        .step-1 { background: var(--primary-color); color: white; box-shadow: 0 0 0 4px rgba(26, 188, 156, 0.2); }
        .step-2 { background: #eee; color: #999; }
        
        .connector { position: absolute; height: 2px; width: 40px; background: #eee; top: 115px; z-index: 0; }

        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; color: var(--text-dark); font-weight: 600; font-size: 14px; }
        
        input {
            width: 100%;
            padding: 12px; border: 2px solid #e0e0e0; border-radius: var(--radius);
            font-size: 15px; transition: all 0.3s;
        }
        input:focus { border-color: var(--primary-color); outline: none; }

        .btn-next {
            width: 100%;
            padding: 14px; background: var(--secondary-color); color: white;
            border: none; border-radius: var(--radius); font-size: 16px; font-weight: 600;
            cursor: pointer; margin-top: 10px;
            transition: all 0.3s;
        }
        .btn-next:hover { background: var(--primary-dark); transform: translateY(-2px); }

        .error-msg { color: var(--danger); font-size: 13px; margin-top: 5px; display: none; }

        .login-link { text-align: center; margin-top: 20px; font-size: 14px; color: var(--text-light); }
        .login-link a { color: var(--primary-color); text-decoration: none; font-weight: bold; cursor: pointer;}
    </style>
</head>
<body>

    <div class="connector"></div>

    <div class="container">
        <div style="text-align: center; margin-bottom: 20px;">
            <img src="/static/img/logo-new.jpg" alt="Logo" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover;">
        </div>

        <h1>Criar Conta</h1>
        <p class="subtitle">Passo 1 de 2 - Seus Dados</p>

        <div class="progress-bar">
            <div class="step step-1">1</div>
            <div class="step step-2">2</div>
        </div>

        <form id="step1Form" onsubmit="goToStep2(event)">
            <div class="form-group">
                <label>Nome Completo</label>
                <input type="text" id="name" placeholder="Ex: João Silva" required>
            </div>

            <div class="form-group">
                <label>CPF</label>
                <input type="text" id="cpf" placeholder="000.000.000-00" required maxlength="14" oninput="mascaraCPF(this)">
            </div>

            <div class="form-group">
                <label>E-mail</label>
                <input type="email" id="email" placeholder="seu@email.com" required>
            </div>

            <div class="form-group">
                <label>Senha</label>
                <input type="password" id="password" placeholder="••••••••" required minlength="6">
            </div>

            <div class="form-group">
                <label>Confirmar Senha</label>
                <input type="password" id="confirmPassword" placeholder="••••••••" required>
                <div class="error-msg" id="passError">As senhas não coincidem!</div>
            </div>

            <button type="submit" class="btn-next">Próximo Passo →</button>
        </form>

        <div class="login-link">
            Já tem uma conta?
            <a href="/login">Fazer Login</a>
        </div>
    </div>

    <script>
        function mascaraCPF(i){
            var v = i.value;
            if(isNaN(v[v.length-1])){
                i.value = v.substring(0, v.length-1);
                return;
            }
            i.setAttribute("maxlength", "14");
            if (v.length == 3 || v.length == 7) i.value += ".";
            if (v.length == 11) i.value += "-";
        }

        function goToStep2(e) {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const cpf = document.getElementById('cpf').value;
            const email = document.getElementById('email').value;
            const pass = document.getElementById('password').value;
            const confirm = document.getElementById('confirmPassword').value;
            if (pass !== confirm) {
                document.getElementById('passError').style.display = 'block';
                return;
            }

            const cpfLimpo = cpf.replace(/\D/g, '');
            if (cpfLimpo.length !== 11) {
                alert('CPF inválido! Digite os 11 números.');
                return;
            }

            const userData = { name, cpf: cpfLimpo, email, pass };
            localStorage.setItem('tempUserData', JSON.stringify(userData));

            window.location.href = '/cadastro/disciplinas';
        }
    </script>
</body>
</html>