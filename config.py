import os

class ConfiguracionBase:
    # Clave secreta para sesiones seguras
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_super_segura'

    # Ruta absoluta a la base de datos SQLite dentro del directorio 'instance'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    RUTA_BD = os.path.join(BASE_DIR, 'instance', 'torneo.db')
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{RUTA_BD}"

    # Desactivar el seguimiento de modificaciones
    SQLALCHEMY_TRACK_MODIFICATIONS = False
