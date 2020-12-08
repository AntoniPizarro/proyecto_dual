#https://docs.python.org/3/library/tk.html

#Importación librerías
from tkinter import *
import Scraping
from PythonToMongo import insertarUno
from Generador_paginas_WEB import crearPagina
import webbrowser

#Configuración de la ventana principal
ventana = Tk()
ventana.geometry("500x600")

#Creación del menú
barraMenu = Menu(ventana)
ventana.config(menu=barraMenu)
scrapMenu = Menu(barraMenu, tearoff=0)
insertarMenu = Menu(barraMenu, tearoff=0)
ayudaMenu = Menu(barraMenu, tearoff=0)

#Configuración de opciones del menú
barraMenu.add_cascade(label="Scrap", menu=scrapMenu)
barraMenu.add_cascade(label="Generar Producto", menu=insertarMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

scrapMenu.add_command(label="Obtener todos los datos", command=lambda: todosDatos(True))

insertarMenu.add_command(label="Generar en sitio WEB", command=lambda: webSite())
insertarMenu.add_command(label="Generar en MongoAtlas", command=lambda: mongo())
insertarMenu.add_command(label="Generar en sitio WEB y MongoAtlas", command=lambda: webMongo())

ayudaMenu.add_command(label="Documentación", command=lambda: webbrowser.open("https://proyectodual.000webhostapp.com/documentacion.html"))

genProd = 0

#Funciones
def webSite():
    global genProd
    genProd = 0
    introducirDatos(True)

def mongo():
    global genProd
    genProd = 1
    introducirDatos(True)

def webMongo():
    global genProd
    genProd = 2
    introducirDatos(True)

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

        archivoLabel.grid(padx=5, pady=5, row=3, column=2)
        archivoInput.grid(padx=5, pady=5, row=4, column=2)
        blanco9.grid(padx=5, pady=5, row=5, column=2)

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

        urlimgLabel.grid_forget()
        urlimgInput.grid_forget()
        blanco7.grid_forget()

        altimgLabel.grid_forget()
        altimgInput.grid_forget()
        blanco8.grid_forget()

        archivoLabel.grid_forget()
        archivoInput.grid_forget()
        blanco9.grid_forget()

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
    global genProd
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
    product = {'modelo' : modeloInput.get(), 'marca' : marcaInput.get(), 'gama' : gamaInput.get(), 'archivo' : archivoInput.get(), 'img_dir' : urlimgInput.get(), 'img_alt' : altimgInput.get(), 'tasa' : tasaInput.get(), 'color' : colorInput.get(), 'plazas' : plazasInput.get(), 'caracteristicas' : caractSelected}
    modeloInput.delete(0, END)
    marcaInput.delete(0, END)
    gamaInput.delete(0, END)
    tasaInput.delete(0, END)
    colorInput.delete(0, END)
    plazasInput.delete(0, END)
    altimgInput.delete(0, END)
    archivoInput.delete(0, END)
    urlimgInput.delete(0, END)
    for estado in estadosCheckBox:
        estado.set(0)
    print(product)
    if genProd == 0:
        crearPagina(product['modelo'], product['marca'], product['archivo'], product['gama'], product['color'], product['img_dir'], product['img_alt'], product['plazas'], product['caracteristicas'], )
    elif genProd == 1:
        insertarUno(product)
    elif genProd == 2:
        crearPagina(product['modelo'], product['marca'], product['archivo'], product['gama'], product['color'], product['img_dir'], product['img_alt'], product['plazas'], product['caracteristicas'], )
        insertarUno(product)

def comprChecks():
    caractCount = 0
    for checks in estadosCheckBox:
        if checks.get() == 1:
            if checks == chekState1:
                caractCount += 1
            elif checks == chekState2:
                caractCount += 1
            elif checks == chekState3:
                caractCount += 1
            elif checks == chekState4:
                caractCount += 1
            elif checks == chekState5:
                caractCount += 1
            elif checks == chekState6:
                caractCount += 1
            elif checks == chekState7:
                caractCount += 1
            elif checks == chekState8:
                caractCount += 1
            elif checks == chekState9:
                caractCount += 1
            elif checks == chekState10:
                caractCount += 1
            elif checks == chekState11:
                caractCount += 1
            elif checks == chekState12:
                caractCount += 1
            elif checks == chekState13:
                caractCount += 1
            elif checks == chekState14:
                caractCount += 1
            elif checks == chekState15:
                caractCount += 1
    if caractCount >= 6:
        for checks in estadosCheckBox:
            if checks.get() == 0:
                if checks == chekState1:
                    caracteristica1.config(state=DISABLED)
                elif checks == chekState2:
                    caracteristica2.config(state=DISABLED)
                elif checks == chekState3:
                    caracteristica3.config(state=DISABLED)
                elif checks == chekState4:
                    caracteristica4.config(state=DISABLED)
                elif checks == chekState5:
                    caracteristica5.config(state=DISABLED)
                elif checks == chekState6:
                    caracteristica6.config(state=DISABLED)
                elif checks == chekState7:
                    caracteristica7.config(state=DISABLED)
                elif checks == chekState8:
                    caracteristica8.config(state=DISABLED)
                elif checks == chekState9:
                    caracteristica9.config(state=DISABLED)
                elif checks == chekState10:
                    caracteristica10.config(state=DISABLED)
                elif checks == chekState11:
                    caracteristica11.config(state=DISABLED)
                elif checks == chekState12:
                    caracteristica12.config(state=DISABLED)
                elif checks == chekState13:
                    caracteristica13.config(state=DISABLED)
                elif checks == chekState14:
                    caracteristica14.config(state=DISABLED)
                elif checks == chekState15:
                    caracteristica15.config(state=DISABLED)
    else:
        caracteristica1.config(state=NORMAL)
        caracteristica2.config(state=NORMAL)
        caracteristica3.config(state=NORMAL)
        caracteristica4.config(state=NORMAL)
        caracteristica5.config(state=NORMAL)
        caracteristica6.config(state=NORMAL)
        caracteristica7.config(state=NORMAL)
        caracteristica8.config(state=NORMAL)
        caracteristica9.config(state=NORMAL)
        caracteristica10.config(state=NORMAL)
        caracteristica11.config(state=NORMAL)
        caracteristica12.config(state=NORMAL)
        caracteristica13.config(state=NORMAL)
        caracteristica14.config(state=NORMAL)
        caracteristica15.config(state=NORMAL)

#Función comodín
def nada():
    print("Función comodín")

#Creación de los elementos de la interfaz
etiqueta1 = Label(ventana, text = "url:")
cajaTexto = Entry(ventana)
etiqueta2 = Label(ventana, text = "")
insercion = Button(ventana, text = "Insertar en la BD", command = lambda: obtenerTodosDatos(cajaTexto.get()))

blanco9 = Label(ventana, text = "")
archivoInput = Entry(ventana, width=10)
archivoLabel = Label(ventana, text = "Nombre archivo:")
blanco8 = Label(ventana, text = "")
altimgInput = Entry(ventana, width=10)
altimgLabel = Label(ventana, text = "Texto alternativo imagen:")
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

#Variables de los Check Box
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

#Declaración de los elementos Check Box
caracteristica1 = Checkbutton(ventana, text="Turbo láser", variable = chekState1, command = lambda: comprChecks())
caracteristica2 = Checkbutton(ventana, text="Cañones de iones", variable = chekState2, command = lambda: comprChecks())
caracteristica3 = Checkbutton(ventana, text="Artillería", variable = chekState3, command = lambda: comprChecks())
caracteristica4 = Checkbutton(ventana, text="Torpedos", variable = chekState4, command = lambda: comprChecks())
caracteristica5 = Checkbutton(ventana, text="Misileros", variable = chekState5, command = lambda: comprChecks())
caracteristica6 = Checkbutton(ventana, text="Escudos", variable = chekState6, command = lambda: comprChecks())
caracteristica7 = Checkbutton(ventana, text="Hipervelocidad", variable = chekState7, command = lambda: comprChecks())
caracteristica8 = Checkbutton(ventana, text="Camuflaje", variable = chekState8, command = lambda: comprChecks())
caracteristica9 = Checkbutton(ventana, text="Patas extensibles", variable = chekState9, command = lambda: comprChecks())
caracteristica10 = Checkbutton(ventana, text="Puente de mando", variable = chekState10, command = lambda: comprChecks())
caracteristica11 = Checkbutton(ventana, text="Cabina", variable = chekState11, command = lambda: comprChecks())
caracteristica12 = Checkbutton(ventana, text="Cámara de carga", variable = chekState12, command = lambda: comprChecks())
caracteristica13 = Checkbutton(ventana, text="Hangar", variable = chekState13, command = lambda: comprChecks())
caracteristica14 = Checkbutton(ventana, text="Puerto", variable = chekState14, command = lambda: comprChecks())
caracteristica15 = Checkbutton(ventana, text="Velas solares", variable = chekState15, command = lambda: comprChecks())

#Cargar todo el código en la ventana principal
print("OK!")
ventana.mainloop()