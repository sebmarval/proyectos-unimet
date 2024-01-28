"pelea pokemon"
import random
Ps_jugador = 100 #Ps es puntos de salud
Ps_oponente = 100
defensa_oponente = 100
defensa_jugador = 100

ataques = { "ataque-jugador1" : "malicioso", "ataque-jugador2" : "placaje", "ataque-jugador3": "ascuas"}

while Ps_jugador > 0 and Ps_oponente > 0:
    ataque_jugador = input("ataque: ")
    ataque_jugador = ataque_jugador.lower() 
    if ataque_jugador == (ataques["ataque-jugador1"]):
        print("has reducido la defensa de tu oponente en 10 puntos")
        defensa_oponente = defensa_oponente - 10
        if defensa_oponente <= 0:
            defensa_oponente = 1
    elif ataque_jugador == (ataques["ataque-jugador2"]):
        print("han reducido enormemente tus puntos")
        Ps_oponente -= 35 * (100/defensa_oponente)
    elif ataque_jugador == (ataques["ataque-jugador3"]):
        print("diste un golpe severo a tu oponente")
        pass
        Ps_oponente -= 20 
    else:
        print("Que estás haciendo?! tus ataques son malicioso, placaje y ascuas!")
        continue
    
    #Turno del oponente 
    #el turno del oponente se define con un random
    ataque_oponente = random.randrange(1,3+1)
    if ataque_oponente == 1: #látigo
        print("has recibido 10 puntos de daño!")
        defensa_jugador -= 10
        if defensa_jugador <= 0:
            defensa_jugador = 1
    elif ataque_oponente == 2: #placaje
        print("han reducido tu salud!")
        Ps_jugador -= 35 * (100/defensa_jugador)
    elif ataque_oponente == 3: #pistola de agua
        print("recibiste un golpe severo!")
        Ps_jugador -= 40
    #randrange está garantizado a ser 1,2 ó 3 
        
#si termina el ciclo, alguien ha ganado
if Ps_oponente <= 0 and Ps_jugador <= 0:
    print("empate!") #
elif Ps_oponente <= 0: #ya sabemos que el jugador es >0
    print("has ganado!") 
else: #ya sabemos que el oponente es > 0
    print("has perdido!")
