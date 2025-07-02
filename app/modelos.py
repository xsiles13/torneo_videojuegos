from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .extensiones import basedatos, login

# Modelo de usuario
class Usuario(UserMixin, basedatos.Model):
    __tablename__ = 'usuario'
    id = basedatos.Column(basedatos.Integer, primary_key=True)
    nombre = basedatos.Column(basedatos.String(100), nullable=False)
    correo = basedatos.Column(basedatos.String(120), unique=True, nullable=False)
    contraseña = basedatos.Column(basedatos.String(200), nullable=False)
    es_administrador = basedatos.Column(basedatos.Boolean, default=False)

    participaciones = basedatos.relationship('Participante', backref='usuario', lazy=True)

    def establecer_contraseña(self, texto_plano):
        self.contraseña = generate_password_hash(texto_plano)

    def verificar_contraseña(self, texto_plano):
        return check_password_hash(self.contraseña, texto_plano)

# Carga de usuario para Flask-Login
@login.user_loader
def cargar_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

# Modelo de juego
class Juego(basedatos.Model):
    __tablename__ = 'juego'
    id = basedatos.Column(basedatos.Integer, primary_key=True)
    nombre = basedatos.Column(basedatos.String(100), nullable=False)
    descripcion = basedatos.Column(basedatos.Text, nullable=True)

    participaciones = basedatos.relationship('Participante', backref='juego', lazy=True)

# Modelo de participación
class Participante(basedatos.Model):
    __tablename__ = 'participante'
    id = basedatos.Column(basedatos.Integer, primary_key=True)
    usuario_id = basedatos.Column(basedatos.Integer, basedatos.ForeignKey('usuario.id'), nullable=False)
    juego_id = basedatos.Column(basedatos.Integer, basedatos.ForeignKey('juego.id'), nullable=False)
    nivel = basedatos.Column(basedatos.String(50), nullable=False)
    puntos = basedatos.Column(basedatos.Integer, nullable=False)
