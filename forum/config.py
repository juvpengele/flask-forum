from forum.utilities.functions import generate_random_str

class Config:
    SECRET_KEY=generate_random_str(30)
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/projects_flask_forum"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER="localhost"    
    MAIL_PORT=1025
    MAIL_USERNAME=None
    MAIL_PASSWORD=None
    MAIL_DEFAULT_SENDER="devforum@example.com"
    
    APP_HOST="http://localhost:5000"
    APP_NAME="Dev Forum"