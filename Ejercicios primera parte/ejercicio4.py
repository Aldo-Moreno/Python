#Tomar un caracter y devolver True si es vocal o False en caso de lo contrario.
letra = input("Ingrese letra: ")

def vocal():
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print (True)
    else:
        print (False)

vocal()
