numero = int(input("ESCRIBE UN NUMERO ENTRE 1 Y 10: "))
nombreFichero = "tabla-"+str(numero)+".txt"
f = open(nombreFichero, "w")
for i in range(0,11):
    f.write(str(numero)+"X"+str(i)+"="+str(numero * i)+"\n")
f.close()
