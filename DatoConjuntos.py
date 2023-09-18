# Crear conjuntos vacíos para cada tipo de dato
clientes = set()
dias = set()
meses = set()
montos = set()
domicilios = set()

salir = 0

while (salir != 1):


    # Pedir al usuario que ingrese los datos
    clientes.add (input("Ingrese el nombre del cliente: "))
    dias.add (input("Ingrese el día de la compra: "))
    meses.add (input("Ingrese el mes de la compra: "))
    montos.add (float(input("Ingrese el monto de la compra: ")))
    domicilios.add(input("Ingrese el domicilio de entrega: "))

    # Imprimir los conjuntos con los datos ingresados   
    print("Cliente:", clientes)
    print("Día:", dias)
    print("Mese:", meses)
    print("Monto:", montos)
    print("Domicilio:", domicilios)

    salir = int (input ("Desea otra factura? 1 no, 2 si: "))
    clientes.clear()
    dias.clear()
    meses.clear()
    montos.clear()
    domicilios.clear()
