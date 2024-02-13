from Vehiculo import Vehiculo

class Barco(Vehiculo):
    def __init__(self, matricula: str, año: int, capacidad: int) -> None:
        super().__init__("Barco", matricula, año, capacidad) 
        