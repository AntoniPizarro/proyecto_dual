#21/11/2020 - 0:55
#https://docs.python.org/3/library/tk.html

import tkinter

ventana = tkinter.Tk() #Crear ventana
ventana.geometry("500x300") #Establecer dimensiones

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

ventana.mainloop() #Mantener ventana abierta