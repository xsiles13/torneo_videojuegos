# 🎮 Torneo de Videojuegos – Aplicación Web con Flask

Aplicación web para la gestión de un torneo de videojuegos. Permite el registro de usuarios, administración de juegos y participantes, y visualización de estadísticas con gráficas interactivas.

---

## 🚀 Tecnologías Utilizadas

- **Python 3**
- **Flask**
- **Flask-WTF**
- **Flask-Login**
- **Flask-Bootstrap**
- **SQLite**
- **Plotly**
- **Bootstrap 5**

---

## 🧰 Requisitos Previos

Asegúrate de tener instalado:

- Python 3.8 o superior
- Git (opcional)
- `pip` (gestor de paquetes de Python)
- Virtualenv (opcional pero recomendado)

---

## 📦 Instalación paso a paso (Ubuntu)

```bash
# 1. Clonar el repositorio o descargar el proyecto
git clone https://github.com/xsiles13/torneo_videojuegos.git
cd torneo_videojuegos

# 2. Crear entorno virtual (opcional pero recomendado)
python3 -m venv entorno
source entorno/bin/activate

# 3. Instalar dependencias
pip install -r requerimientos.txt

# 4. Crear la base de datos SQLite
# (la base de datos se crea automáticamente al ejecutar la app por primera vez)

# 5. Ejecutar la aplicación
python run.py
