"año bisiesto sin ciclos"
def esbisiesto(x):
    if x % 4 != 0:
        return False
    elif x % 4 == 0 and x % 100 == 0 and x % 400 != 0:
        return False
    elif x % 4 == 0 and x % 100 != 0:
        return True
    elif x % 4 == 0 and x % 100 == 0 and x % 400 == 0:
        return True

y = int(input("indica entre 1900 y 2199: "))
if int(y)<1900 or int(y)>2199: 
    print(y,"No es una entrada válida")
elif esbisiesto(y):
    print("es bisiesto")
    cantbisiestos = 1
    for i in range(1900,y):
        if esbisiesto(i):
            cantbisiestos += 1
    print("la cantidad de bisiestos", cantbisiestos)
else: print("no es bisiesto")

