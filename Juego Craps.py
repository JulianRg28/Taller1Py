import random   

#Juego Craps

print("Reglas del juego \n Un par de unos en los dados \n Un total de tres en los dados \n Un total de once en los dados \n Si se Obtiene dos o doce en los datos \n Un total de siete en los dados \n En el resto de situaciones pierdes")

def Lanzamiento_dados1():
 return random.randint(1,6)
def Lanzamiento_dados2():
    return random.randint(1,6)
    
if Lanzamiento_dados1==Lanzamiento_dados2:
    print("Ganaste")
else:
    print("Perdiste")
    
