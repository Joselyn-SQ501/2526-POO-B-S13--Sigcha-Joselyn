# Importa el modelo existente del programa
from modelos.vehiculo import Vehiculo

# Clase de servicio que representa la lógica del sistema de gestión de garaje
class GarajeServicio:

    # Creación de un constructor vacío
    def __init__(self):
        self.__vehiculos: dict[str, Vehiculo] = {} # Atributo privado que almacena los vehículos registrados en un diccionario, cuya clave es la placa

    # Método para registrar o agregar un vehículo
    def agregar_vehiculo(self, placa: str, marca: str, propietario: str) -> Vehiculo:
        placa = (placa or "").strip().upper()
        marca = (marca or "").strip()
        propietario = (propietario or "").strip()

        # Validación de campos obligatorios
        if not placa or not marca or not propietario:
            raise ValueError("Todos los campos son obligatorios.")

        # Validación para evitar placas duplicadas
        if placa in self.__vehiculos:
            raise ValueError("Ya existe un vehículo con esa placa.")

        # Creación del objeto Vehículo
        vehiculo = Vehiculo(placa, marca, propietario)

        # Se guarda el vehículo en el diccionario
        self.__vehiculos[placa] = vehiculo

        return vehiculo

    # Método para eliminar un vehículo del sistema
    def eliminar_vehiculo(self, placa: str):

        # Limpieza del dato recibido
        placa = (placa or "").strip().upper()

        # Validación de la existencia del vehículo
        if placa not in self.__vehiculos:
            raise ValueError("El vehículo no existe.")

        # Eliminación del vehículo
        del self.__vehiculos[placa]

    # Método que retorna la lista de vehículos registrados
    def listar_vehiculos(self) -> list[Vehiculo]:
        # Se convierte el diccionario en una lista de objetos Vehículo
        return list(self.__vehiculos.values())