#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
cantidad_invertir = 0.0
interes_anual = 0.0
numero_anios = 0
cantidad_invertir = float(input("Ingrese cantidad a invertirt: "))
interes_anual = float(input("Interes anual: "))
numero_anios = int (input("Numero de anios: "))

for i in range (numero_anios):
    cantidad_invertir *= (1 + interes_anual / 100) 
    print ("La capital obtenido en el anio",i+1, "fue de ",cantidad_invertir)