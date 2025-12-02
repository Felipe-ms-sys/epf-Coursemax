from app import create_app
from controllers import study_controller

if __name__ == '__main__':
    app = create_app()
    app.run()
