<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - App de Estudos</title>
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
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: var(--bg-gradient);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            overflow-y: auto; 
        }

        .login-container {
            background: var(--white);
            padding: 40px;
            border-radius: 20px;
            box-shadow: var(--shadow);
            width: 100%;
            max-width: 400px;
            animation: slideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        }

        @keyframes slideUp {
            from { opacity: 0; transform: translateY(40px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .logo-container { text-align: center; margin-bottom: 25px; }
        .logo { width: 100px; height: 100px; }

        h1 {
            text-align: center;
            color: var(--text-dark);
            margin-bottom: 8px;
            font-size: 26px;
        }

        .subtitle {
            text-align: center;
            color: var(--text-light);
            margin-bottom: 30px;
            font-size: 14px;
        }

        .form-group { margin-bottom: 20px; }

        label {
            display: block;
            margin-bottom: 8px;
            color: var(--text-dark);
            font-weight: 600;
            font-size: 14px;
        }

        input {
            width: 100%;
            padding: 12px 15px;
            border: 2px solid #e0e0e0;
            border-radius: var(--radius);
            font-size: 15px;
            transition: all 0.3s ease;
            color: var(--text-dark);
        }

        input:focus {
            outline: none;
            border-color: var(--primary-color);
            box-shadow: 0 0 0 4px rgba(26, 188, 156, 0.15);
        }

        .btn-login {
            width: 100%;
            padding: 14px;
            background: var(--bg-gradient);
            color: white;
            border: none;
            border-radius: var(--radius);
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            margin-top: 10px;
        }

        .btn-login:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(26, 188, 156, 0.4);
        }

        .btn-login:active { transform: translateY(0); }

        .register-link, .forgot-password { text-align: center; margin-top: 20px; font-size: 14px; color: var(--text-light); }
        .forgot-password { text-align: right; margin-top: 8px; margin-bottom: 20px; font-size: 13px; }

        a {
            color: var(--primary-color);
            text-decoration: none;
            font-weight: 600;
            cursor: pointer;
            transition: color 0.2s;
        }

        a:hover { color: var(--primary-dark); text-decoration: underline; }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="logo-container">
            <svg class="logo" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                <circle cx="100" cy="100" r="90" fill="#2C3E50"/>
                <circle cx="100" cy="100" r="85" fill="none" stroke="#1ABC9C" stroke-width="4"/>
                <path d="M 65 105 L 95 135 L 145 75" fill="none" stroke="#1ABC9C" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        </div>

        <h1>Bem-vindo!</h1>
        <p class="subtitle">Organize seus estudos de forma simples.</p>

        <form action="/login" method="POST">
            <div class="form-group">
                <label for="email">E-mail</label>
                <input type="email" id="email" placeholder="seu@email.com" required>
            </div>

            <div class="form-group">
                <label for="password">Senha</label>
                <input type="password" id="password" placeholder="••••••••" required>
            </div>

            <div class="forgot-password">
                <a href="#">Esqueceu a senha?</a>
            </div>

            <button type="submit" class="btn-login">Entrar</button>
        </form>

        <div class="register-link">
            Não tem uma conta? <a href="/cadastro">Cadastre-se</a>
        </div>
    </div>

    <script>
        function handleLogin(event) {
            event.preventDefault();
            const email = document.getElementById('email').value;
            
            if (email) {
                const userName = email.split('@')[0];
                const formattedName = userName.charAt(0).toUpperCase() + userName.slice(1);
                
                localStorage.setItem('userName', formattedName);
                localStorage.setItem('userEmail', email);
                
                const container = document.querySelector('.login-container');
                container.style.transform = 'translateY(-20px)';
                container.style.opacity = '0';
                
                setTimeout(() => {
                    window.location.href = 'student_dashboard.html';
                }, 300);
            }
        }
    </script>
</body>
</html>