#Tomar una lista de numeros y devolver el mas grande.
canti = int(raw_input("Cantidad de numeros: "))
numeros = []

for x in range(canti):
    lista = int(raw_input("---> "))
    numeros.append(lista)

n = sorted(numeros)
print "Numero mayor: ", n[-1]

