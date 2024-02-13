from Vehiculo import Vehiculo
from Carro import Carro
from Barco import Barco
from Avion import Avion


registro_final = [{
    "tipo": "carro",
    "matricula": "330H60",
    "año": 2008,
    "capacidad": 6
},
{
    "tipo": "carro",
    "matricula": "H34GAU",
    "año": 2018,
    "capacidad": 5
},
{
    "tipo": "avion",
    "matricula": "NHU871",
    "año": 2015,
    "capacidad": 200    

},
{
    "tipo": "avion",
    "matricula": "DAN39U",
    "año": 2022,
    "capacidad": 600

},
{
    "tipo": "barco",
    "matricula": "UT-71110790GGG1",
    "año": 2002,
    "capacidad": 2000
},
{
    "tipo": "barco",
    "matricula": "IT-EEE679111Y67",
    "año": 2018,
    "capacidad": 3400

}
]   

def registro_vehiculos(registro_vehicular:list):
    carros:list[Vehiculo] = []
    barcos:list[Vehiculo] = []
    aviones:list[Vehiculo] = []
    for vehiculo in registro_vehicular:
        tipo = vehiculo["tipo"]
        matricula = vehiculo["matricula"]
        año = vehiculo["año"]
        capacidad = vehiculo["capacidad"]
        if tipo == "carro":
            carros.append(vehiculo) 
        elif tipo == "avion":
            aviones.append(vehiculo)
        elif tipo == "barco":
            barcos.append(vehiculo)
    print("lista de carros",carros)
    print("lista de barcos",barcos)
    print("lista de aviones",aviones)

c = registro_vehiculos(registro_final)
print(c)   

