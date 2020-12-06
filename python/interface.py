#21/11/2020 - 0:55 / 1:50
#26/11/2020 - 21:31 / 23:27
#https://docs.python.org/3/library/tk.html

from tkinter import *
import Scraping
from PythonToMongo import insertarUno
import Generador_paginas_WEB as gpw

ventana = Tk() #Crear ventana
ventana.geometry("500x600") #Establecer dimensiones
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
genProd = 0
def webSite():
    introducirDatos(True)
    global genProd
    genProd = 0

def mongo():
    introducirDatos(True)
    global genProd
    genProd = 1

def webMongo():
    introducirDatos(True)
    global genProd
    genProd = 2

def introducirDatos(activacion):
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

        urlimgLabel.grid(padx=5, pady=5, row=9, column=1)
        urlimgInput.grid(padx=5, pady=5, row=10, column=1)
        blanco7.grid(padx=5, pady=5, row=11, column=1)

        altimgLabel.grid(padx=5, pady=5, row=9, column=0)
        altimgInput.grid(padx=5, pady=5, row=10, column=0)
        blanco8.grid(padx=5, pady=5, row=12, column=1)

        introducirDatosBoton.grid(padx=5,row=1, column=2)

        caracteristica1.grid(sticky="W",padx=10, pady=5, row=13, column=0)
        caracteristica2.grid(sticky="W",padx=10, pady=5, row=13, column=1)
        caracteristica3.grid(sticky="W",padx=10, pady=5, row=13, column=2)
        caracteristica4.grid(sticky="W",padx=10, pady=5, row=14, column=0)
        caracteristica5.grid(sticky="W",padx=10, pady=5, row=14, column=1)
        caracteristica6.grid(sticky="W",padx=10, pady=5, row=14, column=2)
        caracteristica7.grid(sticky="W",padx=10, pady=5, row=15, column=0)
        caracteristica8.grid(sticky="W",padx=10, pady=5, row=15, column=1)
        caracteristica9.grid(sticky="W",padx=10, pady=5, row=15, column=2)
        caracteristica10.grid(sticky="W",padx=10, pady=5, row=16, column=0)
        caracteristica11.grid(sticky="W",padx=10, pady=5, row=16, column=1)
        caracteristica12.grid(sticky="W",padx=10, pady=5, row=16, column=2)
        caracteristica13.grid(sticky="W",padx=10, pady=5, row=17, column=0)
        caracteristica14.grid(sticky="W",padx=10, pady=5, row=17, column=1)
        caracteristica15.grid(sticky="W",padx=10, pady=5, row=17, column=2)
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
        etiqueta1.grid(padx=10, pady=5, row=0, column=0)
        cajaTexto.grid(padx=10, pady=5, row=0, column=1)
        etiqueta2.grid(padx=10, pady=5, row=1, column=0)
        insercion.grid(padx=10, pady=5, row=2, column=1)
    else:
        etiqueta1.grid_forget()
        cajaTexto.grid_forget()
        etiqueta2.grid_forget()
        insercion.grid_forget()

def obtenerTodosDatos(link):
    Scraping.webCrawler(link)
    cajaTexto.delete(0, END)

def newProduct():
    caractSelected = []
    for checks in estadosCheckBox:
        if checks.get() == 1:
            if checks == chekState1:
                caractSelected.append("Turbo Láser")
            elif checks == chekState2:
                caractSelected.append("Cañones de iones")
            elif checks == chekState3:
                caractSelected.append("Artillería")
            elif checks == chekState4:
                caractSelected.append("Torpedos")
            elif checks == chekState5:
                caractSelected.append("Misileros")
            elif checks == chekState6:
                caractSelected.append("Escudos")
            elif checks == chekState7:
                caractSelected.append("Hipervelocidad")
            elif checks == chekState8:
                caractSelected.append("Camuflaje")
            elif checks == chekState9:
                caractSelected.append("Patas extensibles")
            elif checks == chekState10:
                caractSelected.append("Puente de mando")
            elif checks == chekState11:
                caractSelected.append("Cabina")
            elif checks == chekState11:
                caractSelected.append("Cámara de carga")
            elif checks == chekState13:
                caractSelected.append("Hangar")
            elif checks == chekState14:
                caractSelected.append("Puerto")
            elif checks == chekState15:
                caractSelected.append("Velas solares")
    product = {'modelo' : modeloInput.get(), 'marca' : marcaInput.get(), 'gama' : gamaInput.get(), 'tasa' : tasaInput.get(), 'color' : colorInput.get(), 'plazas' : plazasInput.get(), 'caracteristicas' : caractSelected}
    modeloInput.delete(0, END)
    marcaInput.delete(0, END)
    gamaInput.delete(0, END)
    tasaInput.delete(0, END)
    colorInput.delete(0, END)
    plazasInput.delete(0, END)
    print(product)
    global genProd
    if genProd == 0:
        pass
    elif genProd == 1:
        pass
    elif genProd == 2:
        pass

def nada():
    print("Funcion comodín")
etiqueta1 = Label(ventana, text = "url:")
cajaTexto = Entry(ventana)
etiqueta2 = Label(ventana, text = "")
insercion = Button(ventana, text = "Insertar en la BD", command = lambda: obtenerTodosDatos(cajaTexto.get()))

blanco8 = Label(ventana, text = "")
altimgInput = Entry(ventana, width=10)
altimgLabel = Label(ventana, text = "texto alternativo imagen:")
blanco7 = Label(ventana, text = "")
urlimgInput = Entry(ventana, width=10)
urlimgLabel = Label(ventana, text = "url imagen:")
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
introducirDatosBoton = Button(ventana, height = 2, width = 20, text = "Introducir", command = lambda: newProduct())

chekState1 = IntVar()
chekState2 = IntVar()
chekState3 = IntVar()
chekState4 = IntVar()
chekState5 = IntVar()
chekState6 = IntVar()
chekState7 = IntVar()
chekState8 = IntVar()
chekState9 = IntVar()
chekState10 = IntVar()
chekState11 = IntVar()
chekState12 = IntVar()
chekState13 = IntVar()
chekState14 = IntVar()
chekState15 = IntVar()
estadosCheckBox = [chekState1, chekState2, chekState3, chekState4, chekState5, chekState6, chekState7, chekState8, chekState9, chekState10, chekState11, chekState12, chekState13, chekState14, chekState15]

caracteristica1 = Checkbutton(ventana, text="Turbo láser", variable = chekState1)
caracteristica2 = Checkbutton(ventana, text="Cañones de iones", variable = chekState2)
caracteristica3 = Checkbutton(ventana, text="Artillería", variable = chekState3)
caracteristica4 = Checkbutton(ventana, text="Torpedos", variable = chekState4)
caracteristica5 = Checkbutton(ventana, text="Misileros", variable = chekState5)
caracteristica6 = Checkbutton(ventana, text="Escudos", variable = chekState6)
caracteristica7 = Checkbutton(ventana, text="Hipervelocidad", variable = chekState7)
caracteristica8 = Checkbutton(ventana, text="Camuflaje", variable = chekState8)
caracteristica9 = Checkbutton(ventana, text="Patas extensibles", variable = chekState9)
caracteristica10 = Checkbutton(ventana, text="Puente de mando", variable = chekState10)
caracteristica11 = Checkbutton(ventana, text="Cabina", variable = chekState11)
caracteristica12 = Checkbutton(ventana, text="Cámara de carga", variable = chekState12)
caracteristica13 = Checkbutton(ventana, text="Hangar", variable = chekState13)
caracteristica14 = Checkbutton(ventana, text="Puerto", variable = chekState14)
caracteristica15 = Checkbutton(ventana, text="Velas solares", variable = chekState15)
#C1 = Checkbutton(top, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20)

ventana.mainloop() #Mantener ventana abierta