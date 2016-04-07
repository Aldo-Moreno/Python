n = []

print "Ingrese 5 numeros."
for i in range(5):
    c = int(raw_input("--->" ))
    n.append(c)

print ""
for j in n:
    print "*" * j
