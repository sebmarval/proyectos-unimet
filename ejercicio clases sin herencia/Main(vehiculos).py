from Carro import Carro
from Barco import Barco
from Avion import Avion


registro_final = [{
    "nombre": "Ferrari Roma", 
    "tipo": "carro",
    "matricula": "330H60",
    "año": 2008,
    "capacidad": 4
},
{
    "nombre": "Ford explorer",
    "tipo": "carro",
    "matricula": "H34GAU",
    "año": 2018,
    "capacidad": 6
},
{
    "nombre": "Antonov 225 Mriya",
    "tipo": "avion",
    "matricula": "NHU871",
    "año": 2015,
    "capacidad": 200    

},
{ "nombre": "Airbus 300-600",
    "tipo": "avion",
    "matricula": "DAN39U",
    "año": 2022,
    "capacidad": 600

},
{
    "nombre": "Aventura",
    "tipo": "barco",
    "matricula": "UT-71110790GGG1",
    "año": 2002,
    "capacidad": 2000
},
{
    "nombre": "Disney trip",
    "tipo": "barco",
    "matricula": "IT-EEE679111Y67",
    "año": 2018,
    "capacidad": 3400

}
]   

def registro_vehiculos(registro_vehicular:list):
    carros:list = []
    barcos:list = []
    aviones:list = []
    for vehiculo in registro_vehicular:
        tipo = vehiculo["tipo"]
        matricula = vehiculo["matricula"]
        año = vehiculo["año"]
        capacidad = vehiculo["capacidad"]
        if tipo == "carro":
            carros.append(vehiculo["nombre"]) 
        elif tipo == "avion":
            aviones.append(vehiculo["nombre"])
        elif tipo == "barco":
            barcos.append(vehiculo["nombre"])
    print("lista de carros",carros)
    print("lista de barcos",barcos)
    print("lista de aviones",aviones)

c = registro_vehiculos(registro_final)
print(c)   