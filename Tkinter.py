from tkinter import * #importa el modulo grafico
from tkinter import ttk # importa elementos (widgets)
from tkinter import messagebox #importa messagebox
 
def operar():
    error = False # sera el control de la operacion
    texto = str(combo.get()) # extraemos el item seleccionado
 
    # de acuerdo a la opcion escogia, se realiza una operacion
    if(texto == "Sumar"):
        lbl = Label(root,text="Total: "+str(a.get()+b.get()))
    elif(texto == "Restar"):
        lbl = Label(root,text="Total: "+str(a.get()-b.get()))
    elif(texto=="Multiplicar"):
        lbl = Label(root,text="Total: "+str(a.get() * b.get()))
    # hacemos un try - catch (si se divide entre 0)
    else:
        try:
            lbl = Label(root,text="Total: "+str(round(a.get() / b.get(),2)))
        except:
            messagebox.showerror("Error","No es posible la división entre 0")
            error = True # avisamos que hay error
    # si no hay error, se muestra el resultado
    if(error==False):
        lbl.grid(row=4,column=0)
 
 
root = Tk() #crea la ventana
a = DoubleVar() #maneja el tipo de dato que se usara
b = DoubleVar()
txtA = Entry(root, textvariable=a, width=15) #configuramos los textbox
txtB = Entry(root, textvariable=b, width=15)
# agregamos elementos al combo
combo = ttk.Combobox(root,value=('Sumar','Restar','Multiplicar','Dividir'), takefocus=0)
combo.grid(row=3,column=0)
# creamos el boton y configuramos su accion (command = 'funcion')
btnSumar = Button(root, text="Calcular", command=operar, width=15)
txtA.grid(row=0,column=0)
txtB.grid(row=1,column=0)
btnSumar.grid(row=2,column=0)
root.mainloop() #maneja todo lo que ocurre
 