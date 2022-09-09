from tkinter.ttk import Progressbar
from tkinter import messagebox
from pytube import*
from tkinter import*
import tkinter as tk

windo = tk.Tk()
windo.geometry("520x500")
windo.resizable(False, False)
windo.title("Descargar videos de you tube")
windo.config(background= "#74FF97", relief= "solid", border= 5)

Link = tk.StringVar("")

def Downloading ():
    link_validation = ""
    if len(Link.get()) >= 19:
        for i in range(0,17):
            link_present = Link.get()
            link_validation = link_validation + link_present[i]
        if link_validation == "https://youtu.be/":
            yt = YouTube(Link.get())
            yt.title
            yt.thumbnail_url
            yt.streams
            yt.streams.filter(progressive=True)
            yt.streams.filter(file_extension='mp4')
            stream = yt.streams.get_by_itag(22)
            stream.download(timeout=50)
            messagebox.showinfo(title="Descarga", message="Descarga completada")
        else:
            messagebox.showwarning(title = "Link equivocado", message="Por favor, ingrese un link valido")
    else:
        messagebox.showerror(title = "Error al escribir", message="Por favor, escriba correctamente")  

def about_me_app():
    ventana_about = tk.Toplevel()
    ventana_about.geometry("400x360")
    ventana_about.resizable(False, False)
    ventana_about.configure(bg="#74FF97", relief= "solid", border= 4)
    
    info = tk.Label(ventana_about, text="Desarrollado by: José Montezuma\n Software, descarga videos de YT\n Versión: V.1\n Lanzado: 10/08/2022", font="Rockwell 12 bold italic", bg= "#FFDE59", relief="solid", border= 4)
    info.place(relx= 0.1, rely= 0.2, relheight= 0.4, relwidth= 0.8)
    
    def salida():
        ventana_about.destroy()
    Boton_salida_ventana_about = tk.Button(ventana_about, text= "Salir",command= salida,  font="Rockwell 14 bold", relief="solid", bg="#FF914D", fg="white", border= 3)
    Boton_salida_ventana_about.place(relx= 0.36, rely= 0.7, relheight= 0.1, relwidth= 0.28)

def salida():
    windo.destroy()

def pegar_portapapeles():
    text = windo.clipboard_get()
    Link.set(text)

def limpiarTodo ():
    Entrada_texto.delete("0", "end")

Frame_indicativo = tk.Label(text="Ingrese link:", font="Rockwell 16 bold", bg= "#5CE1E6", relief="solid", border= 3 )
Frame_indicativo.place(relx= 0.1, rely= 0.06, relheight= 0.07, relwidth= 0.3 )

Entrada_texto =  tk.Entry(windo,textvariable = Link, relief="solid",  font="Rockwell 14 bold", border= 4)
Entrada_texto.place(relx= 0.26, rely= 0.16, relheight= 0.08, relwidth= 0.5)

Boton_descargar = tk.Button(windo, text="Descargar", command= Downloading,  font="Rockwell 14 bold", relief="solid", bg="#FD1919", fg="white", border= 3)
Boton_descargar.place(relx= 0.38, rely= 0.28, relheight= 0.09, relwidth= 0.28)

Boton_pegar = tk.Button(windo, text="Pegar", command=pegar_portapapeles,  font="Rockwell 14 bold", relief="solid", bg="#B75BDD", fg="white", border= 3)
Boton_pegar.place(relx= 0.18, rely= 0.45, relheight= 0.09, relwidth= 0.28)

Boton_limpiar = tk.Button(windo, text= "Borrar", command= limpiarTodo, font="Rockwell 14 bold", relief="solid", bg="#B75BDD", fg="white", border= 3)
Boton_limpiar.place(relx= 0.55, rely= 0.45, relheight= 0.09, relwidth= 0.28)

Boton_about = tk.Button(windo, text="About me", command= about_me_app,  font="Rockwell 14 bold", relief="solid", bg="#FF914D", fg="white", border= 3)
Boton_about.place(relx= 0.13, rely= 0.8, relheight= 0.09, relwidth= 0.28)

Boton_salida = tk.Button(windo, text= "Salir",command= salida,  font="Rockwell 14 bold", relief="solid", bg="#FF914D", fg="white", border= 3)
Boton_salida.place(relx= 0.6, rely= 0.8, relheight= 0.09, relwidth= 0.28)

windo.mainloop()