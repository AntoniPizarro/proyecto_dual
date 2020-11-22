#22/11/2020 - 18:56 - 21:07
def obtenerDatos(codigo):
    #Obtenemos los campos de la nave
    modelo = codigo[codigo.find("<h3>") + 4 : codigo.find(" - ")]
    marca = codigo[codigo.find(" - ") + 3 : codigo.find("</h3>")]
    gama = codigo[ codigo.find("<p>Gama:") + 9 : codigo.find(" (Tasa") ]
    tasa = int(codigo[ codigo.find("(Tasa:") + 7 : codigo.find("§") ])
    codigo = codigo[codigo.find("<p>Color:"):] #Arreglamos el codigo para buscar color
    color = codigo[ codigo.find("<p>Color:") + 10 : codigo[ codigo.find("<p>Color:") :].find("</p>") ]
    plazas = int(codigo[ codigo.find("<h2>Numero de plazas: <b>") + 25 : codigo.find("</b>") ])
    codigo = codigo[codigo.find("<div class=\"caracteristicas\">") + 29 :] #Arreglamos el codigo para buscar las caracteristicas
    caracteristicas = []
    #Creamos un loop que guarda las caracteristicas de la nave en una lista
    while codigo.count("<p>") != 0:
        caracteristicas.append(codigo[ codigo.find("<p>") + 3 : codigo.find("</p>") ])
        codigo = codigo[ codigo.find("</p>") + 4: ]
    nave = {'modelo':modelo,'marca':marca,'gama':gama,'tasa':tasa,'color':color,'plazas':plazas,'caracteristicas':caracteristicas}
    return nave