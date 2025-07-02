import os
from app import crear_aplicacion
from app.extensiones import basedatos

# Ruta absoluta del directorio `instance`
directorio_instancia = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')

# Crear el directorio si no existe
os.makedirs(directorio_instancia, exist_ok=True)

# Crear instancia de la aplicación Flask
aplicacion = crear_aplicacion()

# Crear las tablas de la base de datos dentro del contexto de la aplicación
with aplicacion.app_context():
    basedatos.create_all()

# Ejecutar la aplicación
if __name__ == '__main__':
    aplicacion.run(debug=True)
