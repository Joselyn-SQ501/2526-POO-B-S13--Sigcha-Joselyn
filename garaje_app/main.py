from servicios.garaje_servicio import GarajeServicio
from ui.app_tkinter import AppTkinter


def main():

    servicio = GarajeServicio()

    app = AppTkinter(servicio)

    app.run()


if __name__ == "__main__":
    main()