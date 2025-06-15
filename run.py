from app import crear_aplicacion, basedatos
from pathlib import Path

aplicacion = crear_aplicacion()

# Crear la base de datos en /instance la primera vez
with aplicacion.app_context():
    if not Path("instance/torneo.db").exists():
        basedatos.create_all()
        print("✅ Base de datos creada correctamente.")

if __name__ == "__main__":
    aplicacion.run(debug=True)
