from Seller import Seller
from Vehiculo import Vehiculo
from Carro import Carro
from Barco import Barco
from Avion import Avion


registro_final = [{
    "nombre": "Ferrari Roma",
    "tipo": "carro",
    "matricula": "330H60",
    "año": 2008,
    "capacidad": 6,
    "seller": {"nombre": "Ferrari", "ubicacion": "Italia"}
},
{
    "nombre": "Ford explorer",
    "tipo": "carro",
    "matricula": "H34GAU",
    "año": 2018,
    "capacidad": 5,
    "seller": {"nombre": "Ford", "ubicacion": "USA"}
},
{
    "nombre": "Antonov 225 Mriya",
    "tipo": "avion",
    "matricula": "NHU871",
    "año": 2015,
    "capacidad": 200,
    "seller": {"nombre": "Avianca Airlines", "ubicacion": "Venezuela"}    

},
{
    "nombre": "Airbus 300-600",
    "tipo": "avion",
    "matricula": "DAN39U",
    "año": 2022,
    "capacidad": 600,
    "seller": {"nombre": "Laser", "ubicacion": "Venezuela"}

},
{
    "nombre": "Aventura",
    "tipo": "barco",
    "matricula": "UT-71110790GGG1",
    "año": 2002,
    "capacidad": 2000,
    "seller": {"nombre": "Ocean Nagivation Agency", "ubicacion": "USA"}
},
{
    "nombre": "Disney trip",
    "tipo": "barco",
    "matricula": "IT-EEE679111Y67",
    "año": 2018,
    "capacidad": 3400,
    "seller": {"nombre": "Disney", "ubicacion": "USA"}

}
]   
def vender(lista_vehiculos:list[Vehiculo]):
    print("escoja el vehiculo que desea comprar")
    for index, vehiculo in enumerate(lista_vehiculos):
        print(f"{index+1}-{vehiculo}\n")
    opcion = input("Escriba el numero del vehículo que desee comprar: ")
    while not opcion.isnumeric() or int(opcion) <= 0 or int(opcion) > len(lista_vehiculos):
        opcion = input("Ingrese una entrada valida: ")
    vehiculo_escogido = lista_vehiculos[int(opcion)-1]
    vehiculo_escogido.registrar_Venta()

def registro_vehiculos(registro_vehicular:list):
    carros:list[Vehiculo] = []
    barcos:list[Vehiculo] = []
    aviones:list[Vehiculo] = []
    for vehiculo in registro_vehicular:
        seller = vehiculo["seller"]
        nombre = vehiculo["nombre"]
        tipo = vehiculo["tipo"]
        matricula = vehiculo["matricula"]
        año = vehiculo["año"]
        capacidad = vehiculo["capacidad"]
        seller_nombre = seller["nombre"]
        seller_ubicacion = seller["ubicacion"]
        seller_objeto = Seller(seller_nombre, seller_ubicacion)
        if tipo == "carro":
            carro = Carro(nombre, matricula, año, capacidad, seller_objeto)
            carros.append(carro) 
        elif tipo == "avion":
            avion = Avion(nombre, matricula, año, capacidad, seller_objeto)
            aviones.append(avion)
        elif tipo == "barco":
            barco = Barco(nombre, matricula, año, capacidad, seller_objeto)
            barcos.append(barco)
    print("lista de carros",carros)
    print("lista de barcos",barcos)
    print("lista de aviones",aviones)
    return carros+barcos+aviones

vehiculos = registro_vehiculos(registro_final)
vender(vehiculos)

