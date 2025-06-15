# 🎮 Torneo de Videojuegos – Aplicación Web con Flask

Aplicación web para gestionar un torneo de videojuegos, desarrollada con **Python, Flask, SQLite y Plotly**.

Permite el registro de participantes, administración de juegos, puntuaciones, y visualización de estadísticas mediante gráficas interactivas.

## 📦 Tecnologías utilizadas

- Python 3.8+
- Flask
- SQLite
- Plotly
- Bootstrap 5
- Flask-Login para autenticación
- Flask-SQLAlchemy para ORM

## ⚙️ Instalación paso a paso (Ubuntu)

### 1. Clonar el repositorio

```bash
git clone https://github.com/xsiles13/torneo-videojuegos.git
cd torneo-videojuegos
```

### 2. Crear y activar el entorno virtual

```bash
sudo apt update
sudo apt install python3-venv -y

python3 -m venv entorno
source entorno/bin/activate
```

### 3. Instalar dependencias del proyecto

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python run.py
```

Esto ejecutará la aplicación en modo desarrollo y creará automáticamente la base de datos torneo.db en la carpeta database/ si no existe.

Accede desde tu navegador en:
🌐 http://localhost:5000

## Anexo

### 🧪 Usuario administrador

1. Regístrate desde la ruta /registro.

2. Accede al archivo torneo.db usando un editor SQLite como DB Browser for SQLite o vía línea de comandos.

3. En la tabla usuario, cambia el campo rol de "usuario" a "admin".

Esto te dará acceso al panel de administración para crear/editar/eliminar juegos y participantes.

### 📊 Visualización de estadísticas

Accede a /graficas para ver el promedio de puntuaciones por juego.

## 📬 Contacto y soporte

Este proyecto ha sido desarrollado como parte de un ejercicio académico.

Para dudas, mejoras o colaboración, puedes contactarme vía GitHub o correo electrónico.