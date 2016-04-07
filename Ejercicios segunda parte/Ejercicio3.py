cantidad = int(raw_input("Cantidad de palabras: "))
numero   = int(raw_input("Numero: "))
lista    = []

print "Escribe las palabras:"
for x in range(cantidad):
    words = raw_input("---> ")
    lista.append(words)

print ""
print "Palabras mayor que ", numero
for i in lista:
    if len(i) > numero:
        print i
    
