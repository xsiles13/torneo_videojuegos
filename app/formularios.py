from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# Formulario de registro de nuevos usuarios
class FormularioRegistro(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    correo = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    confirmar_contraseña = PasswordField('Confirmar Contraseña', validators=[EqualTo('contraseña')])
    enviar = SubmitField('Registrarse')

# Formulario de inicio de sesión
class FormularioAcceso(FlaskForm):
    correo = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired()])
    recordar = BooleanField('Recordarme')
    enviar = SubmitField('Acceder')

# Formulario para crear o editar juegos
class FormularioJuego(FlaskForm):
    nombre = StringField('Nombre del juego', validators=[DataRequired()])
    enviar = SubmitField('Guardar')

# Formulario para crear o editar participantes
class FormularioParticipante(FlaskForm):
    nombre = StringField('Nombre del participante', validators=[DataRequired()])
    juego_id = SelectField('Juego', coerce=int)
    nivel = SelectField('Nivel', choices=[('amateur', 'Amateur'), ('normal', 'Normal'), ('experto', 'Experto')])
    puntos = IntegerField('Puntos')
    enviar = SubmitField('Guardar')
