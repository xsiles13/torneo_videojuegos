from app import crear_aplicacion

# Crear la aplicación usando la función de fábrica
aplicacion = crear_aplicacion()

# Ejecutar la aplicación en modo de desarrollo
if __name__ == "__main__":
    aplicacion.run(debug=True)
