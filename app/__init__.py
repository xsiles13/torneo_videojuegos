from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from config import ConfiguracionBase

# Inicializar extensiones
basedatos = SQLAlchemy()
login = LoginManager()
bootstrap = Bootstrap()

# Establecer la vista de login por defecto
login.login_view = 'rutas.acceso'

# Función para crear y configurar la aplicación Flask
def crear_aplicacion():
    aplicacion = Flask(__name__)
    aplicacion.config.from_object(ConfiguracionBase)

    # Inicializar extensiones con la aplicación
    basedatos.init_app(aplicacion)
    login.init_app(aplicacion)
    bootstrap.init_app(aplicacion)

    # Importar y registrar el blueprint de rutas
    from app.rutas import rutas_bp
    aplicacion.register_blueprint(rutas_bp)

    return aplicacion
