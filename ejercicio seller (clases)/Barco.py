from Seller import Seller
from Vehiculo import Vehiculo

class Barco(Vehiculo):
    def __init__(self, nombre:str, matricula: str, año: int, capacidad: int, seller:Seller) -> None:
        super().__init__(nombre,"barco", matricula, año, capacidad, seller)
        