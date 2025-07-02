from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedatos = SQLAlchemy()
login = LoginManager()
login.login_view = 'rutas.iniciar_sesion'
