# Clase que representa un vehículo dentro del sistema
class Vehiculo:
    # Constructor de la clase con datos y su tipo
    def __init__(self, placa: str, marca: str, propietario: str):
        self.__placa = placa.strip().upper() # Atributo privado de la placa del vehículo
        self.__marca = marca.strip() # Atributo privado de la marca del vehículo
        self.__propietario = propietario.strip() # Atributo privado del nombre del propietario

    # GETTERS que permiten acceder a los atributos privados de forma controlada
    @property
    def placa(self) -> str:
        return self.__placa

    @property
    def marca(self) -> str:
        return self.__marca

    @property
    def propietario(self) -> str:
        return self.__propietario

    # SETTERS que permiten modificar los atributos validando los datos
    @placa.setter
    def placa(self, nueva_placa: str):
        if not nueva_placa.strip():
            raise ValueError("✖️ La placa no puede estar vacía.")
        # Se limpia el texto y se guarda en mayúsculas
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

    # Método que devuelve la información del vehículo
    def __repr__(self) -> str:
        return f"Vehiculo(placa={self.placa}, marca={self.marca}, propietario={self.propietario})"