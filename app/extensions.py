from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
mail = Mail()

# Login manager settings
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

# Create serializer function
def create_serializer(app):
    return URLSafeTimedSerializer(app.config['SECRET_KEY'])