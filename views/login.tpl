<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - App de Estudos</title>
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

        .logo-container { 
            text-align: center;
            margin-bottom: 25px; 
        }
        
        /* Estilo da Logo Nova */
        .logo { 
            width: 100px; 
            height: 100px;
            border-radius: 50%;
            object-fit: cover; /* Garante que a imagem não distorça */
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

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

        .register-link, .forgot-password { 
            text-align: center; margin-top: 20px; font-size: 14px; color: var(--text-light);
        }
        .forgot-password { 
            text-align: right; margin-top: 8px; margin-bottom: 20px; font-size: 13px;
        }

        a {
            color: var(--primary-color);
            text-decoration: none;
            font-weight: 600;
            cursor: pointer;
            transition: color 0.2s;
        }

        a:hover { 
            color: var(--primary-dark);
            text-decoration: underline; 
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="logo-container">
            <img src="/static/img/logo-new.jpg" alt="Logo CourseMax" class="logo">
        </div>

        <h1>Bem-vindo!</h1>
        <p class="subtitle">Organize seus estudos de forma simples.</p>

        % if defined('error') and error:
            <div style="background-color: #ffcccc; color: #cc0000; padding: 10px; border-radius: 5px; margin-bottom: 15px; text-align: center;">
                {{error}}
            </div>
        % end

        <form action="/login" method="POST">
            <div class="form-group">
                <label for="email">E-mail</label>
                <input type="email" id="email" name="email" placeholder="seu@email.com" required>
            </div>

            <div class="form-group">
                <label for="password">Senha</label>
                <input type="password" id="password" name="password" placeholder="••••••••" required>
            </div>

            <div class="forgot-password">
                <a href="#">Esqueceu a senha?</a>
            </div>

            <button type="submit" class="btn-login">Entrar</button>
        </form>

        <div class="register-link">
            Não tem uma conta?
            <a href="/cadastro">Cadastre-se</a>
        </div>
    </div>

    <script>
        function handleLogin(event) {
            event.preventDefault(); // Nota: O formulário usa action="/login", esse JS é apenas decorativo se não for usado.
            const email = document.getElementById('email').value;
            // A lógica real de login é feita pelo backend (Bottle)
        }
    </script>
</body>
</html>