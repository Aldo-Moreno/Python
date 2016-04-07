canti  = int(raw_input("Cantidad de palabras: "))
lista  = []
ml     = ""

print "Escriba las palabras:"
for i in range(canti):
    words = raw_input("---> ")
    lista.append(words)

for x in lista:
    if len(x) > len(ml):
        ml = x

print "Palabra mas larga: ", ml




    
