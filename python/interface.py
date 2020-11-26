#21/11/2020 - 0:55 / 1:50
#https://docs.python.org/3/library/tk.html

import tkinter
import Scraping
from PythonToMongo import insertarUno

ventana = tkinter.Tk() #Crear ventana
ventana.geometry("200x110") #Establecer dimensiones
"""
etiqueta = tkinter.Label(ventana, text = "Me cago en toh", bg = "green") #Crear etiqueta o texto para mostrar en ventana
etiqueta.pack() #Mostrar etiqueta
etiqueta.pack(side = tkinter.RIGHT) #Mostrar etiqueta a la derecha
etiqueta.pack(side = tkinter.LEFT) #Mostrar etiqueta a la izquierda
etiqueta.pack(side = tkinter.BOTTOM) #Mostrar etiqueta abajo
etiqueta.pack(fill = tkinter.X) #Mostrar etiqueta, reservando una fila para esa etiqueta

def saludo(nombre, num):
    print("Hola, " + nombre + " " + str(num))

def printear(text):
    print(text)

boton = tkinter.Button(ventana, text = "Pulsa para follar", padx = 30, pady = 10, command = lambda: saludo("Idiota", 12)) #Crear un boton en la ventana con el texto personalizado con dimensiones de 30 de largo y 10 de alto que ejecuta la funcion "saludo" con unos parametros
boton.pack() #Mostrar boton

cajaTexto = tkinter.Entry(ventana, font = "Helvetica 20") #Crear un campo de entrada en ventana con una fuente 'Helvetica' de tamaño 20
cajaTexto.pack() #Mostrar campo de entrada
escribir = tkinter.Button(ventana, text = "Mostrar texto", padx = 30, pady = 10, command = lambda: printear(cajaTexto.get())) #Crear un boton en la ventana con el texto personalizado con dimensiones de 30 de largo y 10 de alto que ejecuta la funcion "saludo" con unos parametros
escribir.pack()
"""
def insertarDato(link):
    insertarUno(Scraping.obtenerDatos(Scraping.obtenerCodigo(link)))
    cajaTexto.delete(0, tkinter.END)

etiqueta1 = tkinter.Label(ventana, text = "url")
etiqueta1.pack()
cajaTexto = tkinter.Entry(ventana)
cajaTexto.pack()
etiqueta2 = tkinter.Label(ventana, text = "")
etiqueta2.pack()
insercion = tkinter.Button(ventana, text = "Insertar en la BD", command = lambda: Scraping.webCrawler(cajaTexto.get()))
insercion.pack(side = tkinter.BOTTOM)
'''
campoModelo = tkinter.Entry(ventana)
campoMarca = tkinter.Entry(ventana)
campoTasa = tkinter.Entry(ventana)
campoColor = tkinter.Entry(ventana)
campoGama = tkinter.Entry(ventana)
campoPlazas = tkinter.Entry(ventana)
campoCaracteristicas = tkinter.Entry(ventana)

labelModelo = tkinter.Label(ventana, text = "Modelo")
labelMarca = tkinter.Label(ventana, text = "Marca")
labelTasa = tkinter.Label(ventana, text = "Tasa")
labelColor = tkinter.Label(ventana, text = "Color")
labelGama = tkinter.Label(ventana, text = "Gama")
labelPlazas = tkinter.Label(ventana, text = "Plazas")
labelCaracteristicas = tkinter.Label(ventana, text = "Caracteristicas (,)")

campos = [4, 0]

etiqueta1.grid(row = 0, column = 0, pady = 2)
cajaTexto.grid(row = 1, column = 0, pady = 2)
insercion.grid(row = 2, column = 0, pady = 2)
tkinter.Label(ventana, text = "Campos:").grid(row = 3, column = 0, ipady = 4)
labelModelo.grid(row = campos[0], column = campos[1] + 0, pady = 2)
campoModelo.grid(row = campos[0] + 1, column = campos[1] + 0, pady = 2)
labelMarca.grid(row = campos[0], column = campos[1] + 2, pady = 2)
campoMarca.grid(row = campos[0] + 1, column = campos[1] + 2, pady = 2)
labelTasa.grid(row = campos[0], column = campos[1] + 4, pady = 2)
campoTasa.grid(row = campos[0] + 1, column = campos[1] + 4, pady = 2)
labelColor.grid(row = campos[0] + 2, column = campos[1] + 0, pady = 2)
campoColor.grid(row = campos[0] + 3, column = campos[1] + 0, pady = 2)
labelGama.grid(row = campos[0] + 2, column = campos[1] + 2, pady = 2)
campoGama.grid(row = campos[0] + 3, column = campos[1] + 2, pady = 2)
labelPlazas.grid(row = campos[0] + 2, column = campos[1] + 4, pady = 2)
campoPlazas.grid(row = campos[0] + 3, column = campos[1] + 4, pady = 2)
labelCaracteristicas.grid(row = campos[0] + 4, column = campos[1] + 0, pady = 2)
campoCaracteristicas.grid(row = campos[0] + 5, column = campos[1] + 0, pady = 2)
'''
ventana.mainloop() #Mantener ventana abierta