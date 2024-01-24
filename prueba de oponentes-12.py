"pelea pokemon"
import random
Ps_jugador = 100 #Ps es puntos de salud
Ps_oponente = 100
defensa_oponente = 100
defensa_jugador = 100

ataques = ["malicioso","placaje","ascuas"]

while Ps_jugador > 0 and Ps_oponente > 0:
    ataque_jugador = input("Elige un ataque de entre los tres posibles (malicioso, placaje y ascuas): ") 
    if ataque_jugador == "malicioso":
        defensa_oponente = defensa_oponente - 10
        if defensa_oponente <= 0:
            print("has realizado 10 puntos de daño a tu enemigo")
    elif ataque_jugador == "placaje":
        print("la defensa de tu oponente se ha disminuido")
        Ps_oponente -= 35 / (defensa_oponente/100)
    elif ataque_jugador =="ascuas":
        print("has realizado daño de ascuas")
        Ps_oponente -= 20 
    else:
        print("Que estás haciendo?! tus ataques son malicioso, placaje y ascuas!")
        continue
    
    #Turno del oponente 
    #el turno del oponente se define con un random
    ataque_oponente = random.randrange(1,3)
    if ataque_oponente == 1: #látigo
        print("tu oponente te ha hecho 10 de daño")
        defensa_jugador = defensa_jugador - 10
        if defensa_oponente <= 0:
            defensa_oponente = 1
    elif ataque_oponente == 2: #placaje
        Ps_jugador -= 35 / (defensa_jugador/100)
        print("te han atacado")
    elif ataque_oponente == 3: #pistola de agua
        print("has recibido un fuerte ataque")
        Ps_jugador -= 40
    #randrange está garantizado a ser 1,2 ó 3 
        
#si termina el ciclo, alguien ha ganado
if Ps_oponente <= 0 and Ps_jugador <= 0:
    print("empate!") #
elif Ps_oponente <= 0: #ya sabemos que el jugador es >0
    print("has ganado!") 
else: #ya sabemos que el oponente es > 0
    print("has perdido!")
   

    
