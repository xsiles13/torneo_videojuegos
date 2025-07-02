# 🎮 Aplicación Web para Torneo de Videojuegos

Esta aplicación web permite gestionar un torneo de videojuegos con registro de usuarios, autenticación, administración de juegos y participantes, y visualización de estadísticas mediante gráficas.

## 🧠 Funcionalidades

- Registro e inicio de sesión con autenticación segura

- Panel de administrador para crear/editar/eliminar usuarios y juegos

- Los participantes pueden registrar sus puntuaciones por juego

- Gráficas interactivas con Plotly

- Estilo responsive con Bootstrap y CSS personalizado

## 📂 Estructura principal
```text
run.py             # Ejecuta la aplicación
config.py          # Configuración base
/app               # Lógica de la aplicación
    /templates     # HTMLs con Jinja2 y Bootstrap
    /static/css    # CSS personalizado
/instance          # Carpeta donde se guarda la base de datos SQLite
```
  
## 🔧 Requisitos

- Python 3.10 o superior (funciona en 3.13)
- `virtualenv` instalado

## 📦 Instalación paso a paso (Ubuntu)

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/xsiles13/torneo_videojuegos/
   cd torneo_videojuegos
   ```

2. **Crea y activa un entorno virtual**
   ```bash
   python3 -m venv entorno
   source entorno/bin/activate
   ```

3. **Instala las dependencias**
   ```bash
   pip install -r requerimientos.txt
   ```

 4. **Crear el directorio /instance si no existe**
    ```bash
    mkdir instance
    ```

5. **Ejecutar la aplicación**
   
   - Al ejecutarse la aplicación por primera vez se creará la base de datos automáticamente.

   ```bash
   python run.py
   ```

   - Para acceder a la página busca en tu navegador la siguiente ruta:
     *http://localhost:5000*

## 🧪 Usuario Administrador

- Cuando registres un usuario en la página web puedes modificar manualmente si este usuario es administrador o no con estos pasos:

    ### DB Browser for SQLite

    - Instalamos y ejecutamos el programa
  
      ```bash
      sudo apt install sqlitebrowser
      sqlitebrowser
      ```
  
    - Abrir la base de datos torneo.db (está dentro de la carpeta *instance/* del proyecto) y modificar el campo *es_administrador* a 1
  
    - Guardar los cambios y refrescar página web de la aplicación


