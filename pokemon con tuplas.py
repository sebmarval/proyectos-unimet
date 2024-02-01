"pelea pokemon"
import random
Ps_jugador = (100,100) #Ps es puntos de salud
Ps_oponente = (100,100)
ataques_jugador = {"malicioso": (0,10), 
                   "placaje": (35,0), 
                   "ascuas": (20,0)
                   }
ataques_enemigos = {"látigo": (10,10),
                    "placaje": (35,0),
                    "pistola de agua": (20,0)}


while Ps_jugador[0] > 0 and Ps_oponente[0] > 0:
    ataque_jugador = input("ataque: ")
    if ataque_jugador == "malicioso":
        Ps_oponente = (Ps_oponente[0], Ps_oponente[1] - 10)
        if Ps_oponente[1] <= 0:
                Ps_oponente[1] = (1, Ps_oponente[1])
        elif ataque_jugador == "placaje":
            Ps_oponente = (
                Ps_oponente[0] - 35 / (Ps_oponente[1]/100),
                Ps_oponente[1],

            )
        elif ataque_jugador == "ascuas":
                Ps_oponente: (Ps_oponente[0] - 20, Ps_oponente[1])
        else:
            print("Que estás haciendo?! tus ataques son malicioso, placaje y ascuas!")
            continue
    
    #Turno del oponente 
    # turno del oponente se define con un random
    ataque_oponente = random.randrange(1,3+1)
    if ataque_oponente == 1: #látigo
        print("has recibido 10 puntos de daño!")
        Ps_jugador = (Ps_jugador[0], Ps_jugador[1] - 10)
        if Ps_jugador[1] <= 0:
             Ps_jugador = (Ps_jugador[0], 1)
        elif ataque_oponente == 2: #PLACAJE
             print("han reducido tu salud!")
             Ps_jugador = (
                  Ps_jugador[0] - 35 / (Ps_jugador[1]/100),
                  Ps_jugador[1],
             )
        elif ataque_oponente == 3: # Pistola de agua
             print("recibiste un golpe severo!")
             Ps_jugador -= (Ps_jugador[0] - 40, Ps_jugador[1])
    #randrange está garantizado a ser 1,2 ó 3 
        
#si termina el ciclo, alguien ha ganado
if Ps_oponente[0] <= 0 and Ps_jugador[0] <= 0:
    print("empate!") #
elif Ps_oponente[0] <= 0: #ya sabemos que el jugador es >0
    print("has ganado!") 
else: #ya sabemos que el oponente es > 0
    print("has perdido!")
