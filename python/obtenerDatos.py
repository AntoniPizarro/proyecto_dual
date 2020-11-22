#22/11/2020 - 18:56

#https://proyectodual.000webhostapp.com/transports/t70-xwing.html

import requests

def obtenerCodigo(webCrawler):
    if len(webCrawler) < 1 or type(webCrawler) != str:
        return False
    cabecera = "https://proyectodual.000webhostapp.com/transports"
    if webCrawler.find('https') == -1:
        webCrawler = cabecera + webCrawler
    r = requests.get(webCrawler)
    codigoWeb = r.text
    return codigoWeb

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
    

if __name__ == "__main__":
    assert obtenerDatos(obtenerCodigo("https://proyectodual.000webhostapp.com/transports/ca%C3%B1onera-republica.html")) == False

#<h3> - modelo - marca - </h3>
#<p>Gama: - gama - (Tasa: - tasa - §)</p>
#<p>Color: - color -</p>
#h2>b - plazas
#<div class="caracteristicas"> - caracteristicas - </div>

"""
 <h3>T-70 X-Wing - Resistencia</h3>

            <p>Gama: Baja (Tasa: 15§)</p>

            <p>Color: Gris</p>

            <img class="img" alt="X-Wing de la Resistencia" src="https://lumiere-a.akamaihd.net/v1/images/resistance-x-wing_9433981f.jpeg?region=0%2C0%2C1560%2C878&width=768">

            <h2>Numero de plazas: <b>2</b></p>

                <h3>Características:</h3>

            <!--Características-->

            <div class="caracteristicas">

                <p>Hipervelocidad</p>

                <p>Patas extensibles</p>

                <p>Cabina</p>

            </div>
"""