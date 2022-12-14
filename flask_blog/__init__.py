from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_blog.config import Config
from flask_bcrypt import Bcrypt
from flask_mail import Mail

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()


def create_app():
    app = Flask(__name__)

    from flask_blog.main.routes import main
    app.register_blueprint(main)
    from flask_blog.users.routes import users
    app.register_blueprint(users)
    from flask_blog.posts.routes import posts
    app.register_blueprint(posts)
    from flask_blog.errors.handlers import errors
    app.register_blueprint(errors)

    login_manager.init_app(app)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    return app
