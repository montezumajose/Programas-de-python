#Algoritmo para saber cuanto dias tiene el mes, el cual debe ser escrito por el usuario 
mes =  ""
mes = (input("Escriba un mes del año, por favor: "))
mes = mes.capitalize()
if mes == "Enero":
    print("Enero tiene 31 dias")
elif mes == "Febrero":
    print("Febrero tiene 28 dias")
elif mes == "Marzo":
    print("Marzo tiene 31 dias")
elif mes == "Abril":
    print("Abril tiene 30 dias")
elif mes == "Mayo":
    print("Mayo tiene 31 dias")
elif mes == "Junio":
    print("junio tiene 30 dias")
elif mes == "Julio":
    print("Julio tiene 31 dias")
elif mes == "Agosto":
    print("Agosto tiene 31 dias")
elif mes == "Septiembre":
    print("Septiembre tiene 30 dias")
elif mes == "Octubre":
    print("Octubre tiene 31 dias")
elif mes == "Noviembre":
    print("Noviembre tiene 30 dias")
elif mes == "Diciembre":
    print("Diciembre tiene 31 dias")
else:
    print("Por favor, vuelva intentarlo. Por ejemplo: Enero")