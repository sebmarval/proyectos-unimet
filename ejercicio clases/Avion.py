from Vehiculo import Vehiculo

class Avion(Vehiculo):
    def __init__(self, matricula: str, año: int, capacidad: int) -> None:
        super().__init__("avion", matricula, año, capacidad)
    