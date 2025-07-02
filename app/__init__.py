from flask import Flask
from .extensiones import basedatos, login
from config import ConfiguracionBase
from .rutas import rutas_principales

def crear_aplicacion():
    app = Flask(__name__)
    app.config.from_object(ConfiguracionBase)

    # Inicialización de extensiones
    basedatos.init_app(app)
    login.init_app(app)

    # Registro de rutas
    app.register_blueprint(rutas_principales)

    return app
