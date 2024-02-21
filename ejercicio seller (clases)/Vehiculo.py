#Vehiculo
from Seller import Seller

class Vehiculo:
    def __init__(self, nombre:str,tipo:str,matricula:str,año:int,capacidad:int, seller: Seller) -> None:
        self.seller = seller
        self.nombre = nombre
        self.tipo = tipo
        self.matricula = matricula
        self.año = año
        self.capacidad = capacidad
    def __repr__(self):
        return f"""nombre: {self.nombre} 
seller: {self.seller.nombre}"""
    def registrar_Venta(self):
        print(f"Fue vendido el vehiculo: {self.nombre}")
        self.seller.ventas += 1
    