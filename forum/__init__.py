from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)
modus = Modus(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
csrf = CSRFProtect(app)

from forum.models import User
from forum.modules.auth.routes import auth_blueprint
from forum.modules.main.routes import main_blueprint
from forum.modules.threads.routes import thread_blueprint

login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(thread_blueprint, url_prefix="/threads")
