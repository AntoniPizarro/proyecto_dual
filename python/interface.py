#21/11/2020 - 0:55 / 1:50
#26/11/2020 - 21:31 / 23:27
#https://docs.python.org/3/library/tk.html

from tkinter import *
import Scraping
from PythonToMongo import insertarUno

ventana = Tk() #Crear ventana
ventana.geometry("400x310") #Establecer dimensiones
barraMenu = Menu(ventana)
ventana.config(menu=barraMenu)

scrapMenu = Menu(barraMenu, tearoff=0)
insertarMenu = Menu(barraMenu, tearoff=0)

barraMenu.add_cascade(label="Scrap", menu=scrapMenu)
barraMenu.add_cascade(label="Generar Producto", menu=insertarMenu)

scrapMenu.add_command(label="Obtener todos los datos", command=lambda: todosDatos(True))

insertarMenu.add_command(label="Generar en sitio WEB", command=lambda: webSite())
insertarMenu.add_command(label="Generar en MongoAtlas", command=lambda: mongo())
insertarMenu.add_command(label="Generar en sitio WEB y MongoAtlas", command=lambda: webMongo())

def webSite():
    print("Pendiente de programar")
    introducirDatos(True)
    print("La página WEB debe ser resubida manualmente para actualizarse")

def mongo():
    print("Pendiente de programar")
    introducirDatos(True)

def webMongo():
    print("Pendiente de programar")
    introducirDatos(True)
    print("La página WEB debe ser resubida manualmente para actualizarse")

def introducirDatos(activacion):
    # [ caracteristicas ]

    if activacion == True:
        todosDatos(False)
        modeloLabel.grid(padx=5, pady=5, row=0, column=0)
        modeloInput.grid(padx=5, pady=5, row=1, column=0)
        blanco1.grid(padx=5, pady=5, row=2, column=0)

        marcaLabel.grid(padx=5, pady=5, row=3, column=0)
        marcaInput.grid(padx=5, pady=5, row=4, column=0)
        blanco2.grid(padx=5, pady=5, row=5, column=0)

        gamaLabel.grid(padx=5, pady=5, row=6, column=0)
        gamaInput.grid(padx=5, pady=5, row=7, column=0)
        blanco3.grid(padx=5, pady=5, row=8, column=0)

        tasaLabel.grid(padx=5, pady=5, row=0, column=1)
        tasaInput.grid(padx=5, pady=5, row=1, column=1)
        blanco4.grid(padx=5, pady=5, row=2, column=1)

        colorLabel.grid(padx=5, pady=5, row=3, column=1)
        colorInput.grid(padx=5, pady=5, row=4, column=1)
        blanco5.grid(padx=5, pady=5, row=5, column=1)

        plazasLabel.grid(padx=5, pady=5, row=6, column=1)
        plazasInput.grid(padx=5, pady=5, row=7, column=1)
        blanco6.grid(padx=5, pady=5, row=8, column=1)

        blanco7.grid(padx=5, pady=5, row=4, column=2)
        introducirDatosBoton.grid(padx=10, pady=5, row=4, column=3)
    else:
        modeloLabel.grid_forget()
        modeloInput.grid_forget()
        blanco1.grid_forget()

        marcaLabel.grid_forget()
        marcaInput.grid_forget()
        blanco2.grid_forget()

        gamaLabel.grid_forget()
        gamaInput.grid_forget()
        blanco3.grid_forget()

        tasaLabel.grid_forget()
        tasaInput.grid_forget()
        blanco4.grid_forget()

        colorLabel.grid_forget()
        colorInput.grid_forget()
        blanco5.grid_forget()

        plazasLabel.grid_forget()
        plazasInput.grid_forget()
        blanco6.grid_forget()
        introducirDatosBoton.grid_forget()

def todosDatos(activacion):
    
    if activacion == True:
        introducirDatos(False)
        etiqueta1.pack()
        cajaTexto.pack()
        etiqueta2.pack()
        insercion.pack(side = BOTTOM)
    else:
        etiqueta1.pack_forget()
        cajaTexto.pack_forget()
        etiqueta2.pack_forget()
        insercion.pack_forget()

def obtenerTodosDatos(link):
    Scraping.webCrawler(link)
    cajaTexto.delete(0, END)

def nada():
    print("Funcion comodín")

etiqueta1 = Label(ventana, text = "url")
cajaTexto = Entry(ventana)
etiqueta2 = Label(ventana, text = "")
insercion = Button(ventana, text = "Insertar en la BD", command = lambda: obtenerTodosDatos(cajaTexto.get()))
blanco6 = Label(ventana, text = "")
plazasInput = Entry(ventana, width=10)
plazasLabel = Label(ventana, text = "Plazas:")
blanco5 = Label(ventana, text = "")
colorInput = Entry(ventana, width=10)
colorLabel = Label(ventana, text = "Color:")
blanco4 = Label(ventana, text = "")
tasaInput = Entry(ventana, width=10)
tasaLabel = Label(ventana, text = "Tasa:")
blanco3 = Label(ventana, text = "")
gamaInput = Entry(ventana, width=10)
gamaLabel = Label(ventana, text = "Gama:")
blanco2 = Label(ventana, text = "")
marcaInput = Entry(ventana, width=10)
marcaLabel = Label(ventana, text = "Marca:")
blanco1 = Label(ventana, text = "")
modeloInput = Entry(ventana, width=10)
modeloLabel = Label(ventana, text = "Modelo:")
blanco7 = Label(ventana, text = "")
introducirDatosBoton = Button(ventana, text = "Introducir", command = lambda: nada())

caracteristica1 = Checkbutton(ventana, text="Turbo laser")
caracteristica2 = Checkbutton(ventana, text="Cañones de iones")
caracteristica3 = Checkbutton(ventana, text="Artilleria")
caracteristica4 = Checkbutton(ventana, text="Torpedos")
caracteristica5 = Checkbutton(ventana, text="Misileros")
caracteristica6 = Checkbutton(ventana, text="Escudos")
caracteristica7 = Checkbutton(ventana, text="Hipervelocidad")
caracteristica8 = Checkbutton(ventana, text="Camuflaje")
caracteristica9 = Checkbutton(ventana, text="Patas extensibles")
caracteristica10 = Checkbutton(ventana, text="Puente de mando")
caracteristica11 = Checkbutton(ventana, text="Cabina")
caracteristica12 = Checkbutton(ventana, text="Camara de carga")
caracteristica13 = Checkbutton(ventana, text="Hangar")
caracteristica14 = Checkbutton(ventana, text="Puerto")
caracteristica15 = Checkbutton(ventana, text="Velas solares")

#C1 = Checkbutton(top, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20)

ventana.mainloop() #Mantener ventana abierta