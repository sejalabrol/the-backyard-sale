from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, getenv
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

load_dotenv()
SECRET_KEY = getenv("SECRET_KEY")

DB_NAME = "database.db"
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.app_context().push()
    Bootstrap(app)

    db.init_app(app)
    
    from .views import views
    from .auth import auth
    from .models import User, Post

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    if not path.exists("website/"+DB_NAME):
        db.create_all()
        print("Created Database")

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app