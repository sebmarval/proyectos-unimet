from Seller import Seller
from  Vehiculo import Vehiculo

class Carro(Vehiculo):
    def __init__(self, nombre:str, matricula: str, año: int, capacidad: int, seller:Seller) -> None:
        super().__init__(nombre,"carro", matricula, año, capacidad, seller)
