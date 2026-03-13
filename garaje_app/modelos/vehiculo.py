class Vehiculo:
    def __init__(self, placa: str, marca: str, propietario: str):
        self.__placa = placa.strip().upper()
        self.__marca = marca.strip()
        self.__propietario = propietario.strip()

    # GETTERS
    @property
    def placa(self) -> str:
        return self.__placa

    @property
    def marca(self) -> str:
        return self.__marca

    @property
    def propietario(self) -> str:
        return self.__propietario

    # SETTERS
    @placa.setter
    def placa(self, nueva_placa: str):
        if not nueva_placa.strip():
            raise ValueError("✖️ La placa no puede estar vacía.")
        self.__placa = nueva_placa.strip().upper()

    @marca.setter
    def marca(self, nueva_marca: str):
        if not nueva_marca.strip():
            raise ValueError("✖️ La marca no puede estar vacía.")
        self.__marca = nueva_marca.strip()

    @propietario.setter
    def propietario(self, nuevo_propietario: str):
        if not nuevo_propietario.strip():
            raise ValueError("✖️ El propietario no puede estar vacío.")
        self.__propietario = nuevo_propietario.strip()

    def __repr__(self) -> str:
        return f"Vehiculo(placa={self.placa}, marca={self.marca}, propietario={self.propietario})"