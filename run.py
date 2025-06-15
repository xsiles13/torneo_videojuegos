from app import crear_aplicacion, basedatos
from pathlib import Path
import os

# Crear la aplicación
aplicacion = crear_aplicacion()

# Crear la carpeta 'instance' si no existe
Path("instance").mkdir(exist_ok=True)

# Crear la base de datos si no existe
with aplicacion.app_context():
    if not Path("instance/torneo.db").exists():
        basedatos.create_all()
        print("Base de datos creada correctamente.")

if __name__ == "__main__":
    aplicacion.run(debug=True)
