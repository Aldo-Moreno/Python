L1 = []
L2 = []
print "Escriba las palabras para llenar la primer lista."
for i in range(5):
    p = raw_input("---> ")
    L1.append(p)
    
print ""
print "Escriba las palabras para llenar la segunda lista."
print "=========================================================================="
for j in range(5):
    w = raw_input("---> ")
    L2.append(w)
    
print ""
print ("Lista no. 1 = ", L1)
print ""
print ("Lista no. 2 = ", L2)

print ""
def aviso():
    print "Hay elementos repetidos."
    exit()

for x in L1:
    for y in L2:
        if x == y:
            aviso()
            break

print "No hay elementos repetidos."       

