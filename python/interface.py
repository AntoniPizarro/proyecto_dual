#21/11/2020 - 0:55 / 1:50
#26/11/2020 - 21:31 / 23:27
#https://docs.python.org/3/library/tk.html

from tkinter import *
import Scraping
from PythonToMongo import insertarUno

ventana = Tk() #Crear ventana
ventana.geometry("400x600") #Establecer dimensiones
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

        caracteristica1.grid(sticky="W",padx=10, pady=5, row=2, column=4)
        caracteristica2.grid(sticky="W",padx=10, pady=5, row=3, column=4)
        caracteristica3.grid(sticky="W",padx=10, pady=5, row=4, column=4)
        caracteristica4.grid(sticky="W",padx=10, pady=5, row=5, column=4)
        caracteristica5.grid(sticky="W",padx=10, pady=5, row=6, column=4)
        caracteristica6.grid(sticky="W",padx=10, pady=5, row=7, column=4)
        caracteristica7.grid(sticky="W",padx=10, pady=5, row=8, column=4)
        caracteristica8.grid(sticky="W",padx=10, pady=5, row=9, column=4)
        caracteristica9.grid(sticky="W",padx=10, pady=5, row=10, column=4)
        caracteristica10.grid(sticky="W",padx=10, pady=5, row=11, column=4)
        caracteristica11.grid(sticky="W",padx=10, pady=5, row=12, column=4)
        caracteristica12.grid(sticky="W",padx=10, pady=5, row=13, column=4)
        caracteristica13.grid(sticky="W",padx=10, pady=5, row=14, column=4)
        caracteristica14.grid(sticky="W",padx=10, pady=5, row=15, column=4)
        caracteristica15.grid(sticky="W",padx=10, pady=5, row=16, column=4)
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

        caracteristica1.grid_forget()
        caracteristica2.grid_forget()
        caracteristica3.grid_forget()
        caracteristica4.grid_forget()
        caracteristica5.grid_forget()
        caracteristica6.grid_forget()
        caracteristica7.grid_forget()
        caracteristica8.grid_forget()
        caracteristica9.grid_forget()
        caracteristica10.grid_forget()
        caracteristica11.grid_forget()
        caracteristica12.grid_forget()
        caracteristica13.grid_forget()
        caracteristica14.grid_forget()
        caracteristica15.grid_forget()

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

listaCaracteristicas = []
for i in range(15):
    option = IntVar()
    option.set(0)
    listaCaracteristicas.append(option)
caracteristica1 = Checkbutton(ventana, text="Turbo laser", variable = listaCaracteristicas[0])
caracteristica2 = Checkbutton(ventana, text="Cañones de iones", variable = listaCaracteristicas[1])
caracteristica3 = Checkbutton(ventana, text="Artilleria", variable = listaCaracteristicas[2])
caracteristica4 = Checkbutton(ventana, text="Torpedos", variable = listaCaracteristicas[3])
caracteristica5 = Checkbutton(ventana, text="Misileros", variable = listaCaracteristicas[4])
caracteristica6 = Checkbutton(ventana, text="Escudos", variable = listaCaracteristicas[5])
caracteristica7 = Checkbutton(ventana, text="Hipervelocidad", variable = listaCaracteristicas[6])
caracteristica8 = Checkbutton(ventana, text="Camuflaje", variable = listaCaracteristicas[7])
caracteristica9 = Checkbutton(ventana, text="Patas extensibles", variable = listaCaracteristicas[8])
caracteristica10 = Checkbutton(ventana, text="Puente de mando", variable = listaCaracteristicas[9])
caracteristica11 = Checkbutton(ventana, text="Cabina", variable = listaCaracteristicas[10])
caracteristica12 = Checkbutton(ventana, text="Camara de carga", variable = listaCaracteristicas[11])
caracteristica13 = Checkbutton(ventana, text="Hangar", variable = listaCaracteristicas[12])
caracteristica14 = Checkbutton(ventana, text="Puerto", variable = listaCaracteristicas[13])
caracteristica15 = Checkbutton(ventana, text="Velas solares", variable = listaCaracteristicas[14])

#C1 = Checkbutton(top, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20)

ventana.mainloop() #Mantener ventana abierta