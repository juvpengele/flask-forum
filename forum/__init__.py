from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_bcrypt import Bcrypt
from forum.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
modus = Modus(app)
bcrypt = Bcrypt(app)

from forum.modules.auth.routes import auth_blueprint
from forum.modules.main.routes import main_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)
