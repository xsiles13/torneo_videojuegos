from app import basedatos
from flask_login import UserMixin
from app import login

# Modelo para los usuarios del sistema
class Usuario(basedatos.Model, UserMixin):
    id = basedatos.Column(basedatos.Integer, primary_key=True)
    nombre = basedatos.Column(basedatos.String(64), nullable=False)
    correo = basedatos.Column(basedatos.String(120), unique=True, nullable=False)
    contraseña = basedatos.Column(basedatos.String(128))
    es_administrador = basedatos.Column(basedatos.Boolean, default=False)

# Modelo para los juegos del torneo
class Juego(basedatos.Model):
    id = basedatos.Column(basedatos.Integer, primary_key=True)
    nombre = basedatos.Column(basedatos.String(100), nullable=False)

# Modelo para los participantes en el torneo
class Participante(basedatos.Model):
    id = basedatos.Column(basedatos.Integer, primary_key=True)
    nombre = basedatos.Column(basedatos.String(100), nullable=False)
    juego_id = basedatos.Column(basedatos.Integer, basedatos.ForeignKey('juego.id'))
    nivel = basedatos.Column(basedatos.String(20))  # amateur, normal, experto
    puntos = basedatos.Column(basedatos.Integer, default=0)

# Cargar usuario por ID (necesario para Flask-Login)
@login.user_loader
def cargar_usuario(id):
    return Usuario.query.get(int(id))
