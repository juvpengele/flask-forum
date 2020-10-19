from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_seeder import FlaskSeeder
from flask_debugtoolbar import DebugToolbarExtension
from flask_modus import Modus
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_wtf.csrf import CSRFProtect
from forum.config import Config


app = Flask(__name__, static_folder="public")
app.config.from_object(Config)


db = SQLAlchemy(app)
ma = Marshmallow(app)
modus = Modus(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
csrf = CSRFProtect(app)
migrate = Migrate(app, db)
toolbar = DebugToolbarExtension(app)

seeder = FlaskSeeder()
seeder.init_app(app, db)

from forum.database.models import User
from forum.apps.auth.routes import auth_blueprint
from forum.apps.main.routes import main_blueprint
from forum.apps.threads.routes import thread_blueprint
from forum.apps.comments.routes import comments_blueprint
from forum.apps.settings.routes import settings_blueprint

from forum.src.utilities.helpers import cached_categories

login_manager = LoginManager(app)
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


from forum.database.models.category import Category

@app.context_processor
def inject_categories():
    categories = []
    try:
        categories = cached_categories()
    except e:
        print(e)
        
    return dict(app_categories=categories)


app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(thread_blueprint, url_prefix="/threads")
app.register_blueprint(comments_blueprint, url_prefix="/api")
app.register_blueprint(settings_blueprint, url_prefix="/settings")

# seeders
from forum.database.seeds.category_seeder import CategorySeeder
