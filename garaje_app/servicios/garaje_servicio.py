from modelos.vehiculo import Vehiculo


class GarajeServicio:

    def __init__(self):
        self.vehiculos: dict[str, Vehiculo] = {}

    def agregar_vehiculo(self, placa: str, marca: str, propietario: str) -> Vehiculo:
        placa = (placa or "").strip().upper()
        marca = (marca or "").strip()
        propietario = (propietario or "").strip()

        if not placa or not marca or not propietario:
            raise ValueError("Todos los campos son obligatorios.")

        if placa in self.vehiculos:
            raise ValueError("Ya existe un vehículo con esa placa.")

        vehiculo = Vehiculo(placa, marca, propietario)

        self.vehiculos[placa] = vehiculo

        return vehiculo

    def eliminar_vehiculo(self, placa: str):

        placa = (placa or "").strip().upper()

        if placa not in self.vehiculos:
            raise ValueError("El vehículo no existe.")

        del self.vehiculos[placa]

    def listar_vehiculos(self) -> list[Vehiculo]:
        return list(self.vehiculos.values())