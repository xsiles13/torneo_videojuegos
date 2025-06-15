from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import basedatos
from app.modelos import Usuario, Juego, Participante
from app.formularios import FormularioRegistro, FormularioAcceso, FormularioJuego, FormularioParticipante
import plotly.graph_objs as go
import plotly.offline as pyo

rutas_bp = Blueprint('rutas', __name__)

# Página principal
@rutas_bp.route('/')
def inicio():
    return render_template('inicio.html')

# Registro de usuarios
@rutas_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    formulario = FormularioRegistro()
    if formulario.validate_on_submit():
        usuario = Usuario(
            nombre=formulario.nombre.data,
            correo=formulario.correo.data,
            contraseña=generate_password_hash(formulario.contraseña.data),
            es_administrador=False
        )
        basedatos.session.add(usuario)
        basedatos.session.commit()
        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('rutas.acceso'))
    return render_template('registro.html', formulario=formulario)

# Inicio de sesión
@rutas_bp.route('/acceso', methods=['GET', 'POST'])
def acceso():
    formulario = FormularioAcceso()
    if formulario.validate_on_submit():
        usuario = Usuario.query.filter_by(correo=formulario.correo.data).first()
        if usuario and check_password_hash(usuario.contraseña, formulario.contraseña.data):
            login_user(usuario, remember=formulario.recordar.data)
            return redirect(url_for('rutas.panel'))
        flash('Credenciales incorrectas.', 'danger')
    return render_template('acceso.html', formulario=formulario)

# Cerrar sesión
@rutas_bp.route('/salir')
@login_required
def salir():
    logout_user()
    return redirect(url_for('rutas.inicio'))

# Panel de usuario (admin o participante)
@rutas_bp.route('/panel')
@login_required
def panel():
    return render_template('panel.html', usuario=current_user)

# CRUD de juegos (solo admin)
@rutas_bp.route('/admin/juegos', methods=['GET', 'POST'])
@login_required
def gestionar_juegos():
    if not current_user.es_administrador:
        return redirect(url_for('rutas.panel'))

    formulario = FormularioJuego()
    if formulario.validate_on_submit():
        juego = Juego(nombre=formulario.nombre.data)
        basedatos.session.add(juego)
        basedatos.session.commit()
        flash('Juego añadido con éxito', 'success')
        return redirect(url_for('rutas.gestionar_juegos'))

    juegos = Juego.query.all()
    return render_template('administrador/gestionar_juegos.html', formulario=formulario, juegos=juegos)

# CRUD de participantes (solo admin)
@rutas_bp.route('/admin/participantes', methods=['GET', 'POST'])
@login_required
def gestionar_participantes():
    if not current_user.es_administrador:
        return redirect(url_for('rutas.panel'))

    formulario = FormularioParticipante()
    formulario.juego_id.choices = [(j.id, j.nombre) for j in Juego.query.all()]

    if formulario.validate_on_submit():
        participante = Participante(
            nombre=formulario.nombre.data,
            juego_id=formulario.juego_id.data,
            nivel=formulario.nivel.data,
            puntos=formulario.puntos.data
        )
        basedatos.session.add(participante)
        basedatos.session.commit()
        flash('Participante añadido con éxito', 'success')
        return redirect(url_for('rutas.gestionar_participantes'))

    participantes = Participante.query.all()
    return render_template('administrador/gestionar_usuarios.html', formulario=formulario, participantes=participantes)

# Visualización de estadísticas con Plotly
@rutas_bp.route('/graficas')
@login_required
def graficas():
    participantes = Participante.query.all()
    nombres = [p.nombre for p in participantes]
    puntos = [p.puntos for p in participantes]

    grafica = go.Bar(x=nombres, y=puntos, name='Puntos obtenidos')
    layout = go.Layout(title='Puntos por participante')
    figura = go.Figure(data=[grafica], layout=layout)
    grafico_html = pyo.plot(figura, output_type='div')

    return render_template('grafico.html', grafico_html=grafico_html)
