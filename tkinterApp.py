from tkinter import*
from tkinter import messagebox
#configuration de la ventana

ventana = Tk()
ventana.geometry ("300x200")
ventana.config(background="Black")
ventana.title ("Caja-Day off sale")
ventana.config(cursor="spider")


#Variables

precio = DoubleVar()
resul = StringVar()

#funtion 1, aqui se ejecuta el problema y da el resultado

def resultado():
    if  float (precio.get()) >= float(151):
        descuento = float (precio.get()) * float (0.15)
        resultado = float (precio.get()) - float (descuento)
        resultado = float (round (resultado,2))
        return resul.set(resultado)
    elif float (precio.get()) <= float (150):
        descuento = float (precio.get()) * float(0.1)
        resultado = float(precio.get()) - float (descuento)
        resultado = round (resultado,2)
        return resul.set (resultado)
    else:
       print (messagebox.showinfo(message= "Por favor introduzca un precio", title="Error"))


#Entradas

precioentry= Entry(ventana, textvariable= precio, font=("Swift",10,"bold"),bg="#00fa9a", width= 18 )
precioentry.grid(row=0, column= 1,padx= 10, pady= 10)

#Botones

resultado = Button(ventana,text= "Iniciar",font=("Swift",10,"bold"),bg="#00ff00", command= resultado)
resultado.grid(row= 2, column=1,padx= 10, pady= 10)

#Etiquetas

etiqueta_for_precio = Label(ventana,text="Ingrese Precio: ",bg="#ffa500" ,font= ('Swift',10,"bold"))
etiqueta_for_precio.grid(row=0, column= 0)

etiqueta_total = Label(text="Total a Pagar: ",bg="#ffa500", font=("Swift",10,"bold"))
etiqueta_total.grid(row=1,column=0,padx= 10, pady= 10)

total_= Label(ventana, bg= "#7fffd4", textvariable=resul,width=15,font=("Swift",10,"bold"))
total_.grid(row=1,column=1,padx= 10, pady= 10)


#Refreca la venta
ventana.mainloop()