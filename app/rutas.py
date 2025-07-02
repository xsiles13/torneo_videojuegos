from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from app.modelos import Usuario, Juego, Participante
from app.extensiones import basedatos
from werkzeug.security import generate_password_hash, check_password_hash
import plotly.graph_objs as go
import plotly.offline as pyo

rutas_principales = Blueprint('rutas', __name__)

# Página de inicio
@rutas_principales.route('/')
def inicio():
    return render_template('inicio.html')

# Registro de usuario
@rutas_principales.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        if Usuario.query.filter_by(correo=correo).first():
            flash('Este correo ya está registrado.', 'danger')
            return redirect(url_for('rutas.registro'))

        usuario = Usuario(nombre=nombre, correo=correo)
        usuario.establecer_contraseña(contraseña)
        basedatos.session.add(usuario)
        basedatos.session.commit()
        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('rutas.iniciar_sesion'))

    return render_template('registro.html')

# Inicio de sesión
@rutas_principales.route('/login', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        usuario = Usuario.query.filter_by(correo=correo).first()

        if usuario and usuario.verificar_contraseña(contraseña):
            login_user(usuario)
            flash('Sesión iniciada correctamente.', 'success')
            return redirect(url_for('rutas.panel_admin' if usuario.es_administrador else 'rutas.perfil'))
        else:
            flash('Correo o contraseña incorrectos.', 'danger')

    return render_template('login.html')

# Cierre de sesión
@rutas_principales.route('/logout')
@login_required
def cerrar_sesion():
    logout_user()
    flash('Sesión cerrada.', 'info')
    return redirect(url_for('rutas.inicio'))

# Panel de administrador
@rutas_principales.route('/admin')
@login_required
def panel_admin():
    if not current_user.es_administrador:
        flash('Acceso restringido solo para administradores.', 'danger')
        return redirect(url_for('rutas.inicio'))

    usuarios = Usuario.query.all()
    juegos = Juego.query.all()
    return render_template('panel_admin.html', usuarios=usuarios, juegos=juegos)

# Crear juego
@rutas_principales.route('/admin/juego/crear', methods=['GET', 'POST'])
@login_required
def crear_juego():
    if not current_user.es_administrador:
        flash('Acceso restringido.', 'danger')
        return redirect(url_for('rutas.inicio'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        if nombre:
            nuevo_juego = Juego(nombre=nombre)
            basedatos.session.add(nuevo_juego)
            basedatos.session.commit()
            flash('Juego creado con éxito.', 'success')
            return redirect(url_for('rutas.panel_admin'))
        flash('El nombre no puede estar vacío.', 'warning')

    return render_template('crear_juego.html')

# Editar juego
@rutas_principales.route('/admin/juego/editar/<int:id_juego>', methods=['GET', 'POST'])
@login_required
def editar_juego(id_juego):
    if not current_user.es_administrador:
        flash('Acceso denegado.', 'danger')
        return redirect(url_for('rutas.inicio'))

    juego = Juego.query.get_or_404(id_juego)
    if request.method == 'POST':
        nombre = request.form['nombre']
        if nombre:
            juego.nombre = nombre
            basedatos.session.commit()
            flash('Juego actualizado con éxito.', 'success')
            return redirect(url_for('rutas.panel_admin'))
        flash('El nombre no puede estar vacío.', 'warning')

    return render_template('editar_juego.html', juego=juego)

# Eliminar juego
@rutas_principales.route('/admin/juego/eliminar/<int:id_juego>')
@login_required
def eliminar_juego(id_juego):
    if not current_user.es_administrador:
        flash('Acceso denegado.', 'danger')
        return redirect(url_for('rutas.inicio'))

    juego = Juego.query.get_or_404(id_juego)

    # Eliminar participaciones asociadas al juego
    participaciones = Participante.query.filter_by(juego_id=id_juego).all()
    for participacion in participaciones:
        basedatos.session.delete(participacion)

    basedatos.session.delete(juego)
    basedatos.session.commit()
    flash('Juego y sus participaciones eliminados correctamente.', 'info')
    return redirect(url_for('rutas.panel_admin'))


# Eliminar usuario
@rutas_principales.route('/eliminar_usuario/<int:id_usuario>')
@login_required
def eliminar_usuario(id_usuario):
    if not current_user.es_administrador:
        flash('Acceso denegado.', 'danger')
        return redirect(url_for('rutas.inicio'))

    usuario = Usuario.query.get_or_404(id_usuario)

    participaciones = Participante.query.filter_by(usuario_id=id_usuario).all()
    for participacion in participaciones:
        basedatos.session.delete(participacion)

    basedatos.session.delete(usuario)
    basedatos.session.commit()
    flash('Usuario y sus participaciones eliminados.', 'info')
    return redirect(url_for('rutas.panel_admin'))

# Editar usuario
@rutas_principales.route('/admin/usuario/editar/<int:id_usuario>', methods=['GET', 'POST'])
@login_required
def editar_usuario(id_usuario):
    if not current_user.es_administrador:
        flash("Acceso denegado.", "danger")
        return redirect(url_for('rutas.inicio'))

    usuario = Usuario.query.get_or_404(id_usuario)

    if request.method == 'POST':
        nuevo_nombre = request.form['nombre']
        nuevo_correo = request.form['correo']
        if nuevo_nombre and nuevo_correo:
            usuario.nombre = nuevo_nombre
            usuario.correo = nuevo_correo
            basedatos.session.commit()
            flash('Usuario actualizado correctamente.', 'success')
            return redirect(url_for('rutas.panel_admin'))
        else:
            flash('Nombre y correo no pueden estar vacíos.', 'warning')

    return render_template('editar_usuario.html', usuario=usuario)

# Perfil de usuario
@rutas_principales.route('/perfil')
@login_required
def perfil():
    participaciones = Participante.query.filter_by(usuario_id=current_user.id).all()
    juegos_participados_ids = {p.juego_id for p in participaciones}
    juegos_disponibles = Juego.query.filter(~Juego.id.in_(juegos_participados_ids)).all()

    return render_template('perfil.html', participaciones=participaciones, juegos_disponibles=juegos_disponibles)

# Registrar puntuación
@rutas_principales.route('/participar/<int:id_juego>', methods=['GET', 'POST'])
@login_required
def registrar_puntuacion(id_juego):
    juego = Juego.query.get_or_404(id_juego)

    if request.method == 'POST':
        nivel = request.form['nivel']
        puntos = int(request.form['puntos'])

        nueva_participacion = Participante(
            usuario_id=current_user.id,
            juego_id=juego.id,
            nivel=nivel,
            puntos=puntos
        )
        basedatos.session.add(nueva_participacion)
        basedatos.session.commit()
        flash('Puntuación registrada con éxito.', 'success')
        return redirect(url_for('rutas.perfil'))

    return render_template('registrar_puntuacion.html', juego=juego)

# Gráfica de puntos por juego
@rutas_principales.route('/graficas')
def graficas():
    participaciones = Participante.query.join(Usuario).join(Juego).all()

    # Tomar las 3 participaciones con mayor puntuación
    top3_participaciones = sorted(participaciones, key=lambda p: p.puntos, reverse=True)[:3]

    if not top3_participaciones:
        return render_template('graficas.html', top3=[], grafico_html=None)

    # Preparar datos para gráfica
    etiquetas = [f"{p.usuario.nombre} - {p.juego.nombre}" for p in top3_participaciones]
    puntos = [p.puntos for p in top3_participaciones]

    # Gráfica de barras
    fig = go.Figure(data=[go.Bar(
        x=etiquetas,
        y=puntos,
        marker=dict(color='green')
    )])
    fig.update_layout(
        title='Top 3 Participaciones con Mayor Puntuación',
        xaxis_title='Jugador - Juego',
        yaxis_title='Puntos'
    )

    grafico_html = pyo.plot(fig, output_type='div', include_plotlyjs=False)

    # Pasar datos al template
    top3 = list(zip(etiquetas, puntos))

    return render_template('graficas.html', top3=top3, grafico_html=grafico_html)
