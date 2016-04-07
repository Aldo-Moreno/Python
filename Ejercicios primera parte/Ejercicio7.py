word = raw_input("Ingrese palabra o frase: ")
m = word.lower()
se = m.replace(" ","")

def inv():
    volt = list(se)
    volt.reverse()
    e = ("")
    e.join(volt)
    p = e.join(volt)
    if p == word:
        print ("Esta palabra es palindroma")
    else:
        print ("Esta palabra no es palindroma")
    
inv()

