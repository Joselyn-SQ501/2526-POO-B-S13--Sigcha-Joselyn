"""
Sistema Básico de Gestión de Garaje

Aplicación de escritorio desarrollada en Python utilizando la librería Tkinter
para la construcción de la interfaz gráfica. El sistema permite registrar, visualizar y eliminar vehículos dentro de un garaje,
aplicando principios de Programación Orientada a Objetos (POO) y una arquitectura
modular organizada en capas.

"""

# Importa la clase de servicio y la interfaz gráfica
from servicios.garaje_servicio import GarajeServicio
from ui.app_tkinter import AppTkinter

# Función principal del sistema
def main():

    # Se crea la instancia del servicio
    servicio = GarajeServicio()
    # Se crea la aplicación gráfica y se le pasa el servicio
    app = AppTkinter(servicio)
    # Se inicia la aplicación
    app.run()

# Punto de entrada del programa, que llama a la función main para iniciar el sistema
if __name__ == "__main__":
    main()