n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))
n3 = int(input("Ingrese tercer numero: "))

def mayor_de_tres():
    if n1 > n2 and n1 > n3:
        print (n1, " es el numero mayor.")
    elif n2 > n1 and n2 > n3:
        print (n2, " es el numero mayor.")
    elif n3 > n1 and n3 > n2:
        print (n3, " es el numero mayor.")
    else:
        print ("Son iguales.")

mayor_de_tres()
        
