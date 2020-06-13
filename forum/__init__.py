from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from forum.modules.auth.routes import auth_blueprint
from forum.modules.main.routes import main_blueprint
from forum.config import Config

db = SQLAlchemy()
modus = Modus()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    modus.init_app(app)

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    return app