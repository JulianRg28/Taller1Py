edad=int(input("Ingresa tu edad en años \n"))
if 0<=edad<=4:
    print("El cliente ingresa gratis")
if 5<=edad<=18:
    print("El cliente paga $20.000")
if 18<=edad<=60:
    print("El cliente debe pagar $15.000")
if edad>60:
    print("El cliente paga $3.000")
                