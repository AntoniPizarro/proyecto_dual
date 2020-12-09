# Obtener codigo html

import requests
from repository.PythonToMongo import insertarUno

# insertarUno(obtenerDatos(obtenerCodigo("https://proyectodual.000webhostapp.com/transports/y-wing.html")))


def obtenerCodigo(webCrawler):
    # Guardamos el link de cabecera en una variable y el link en caso de que no se encuentre la página o detecte un error en otra variable
    cabecera = "https://proyectodual.000webhostapp.com/"
    inexistent = requests.get(
        "https://proyectodual.000webhostapp.com/1981781ji98p7654yrtgfhjkliop897i6u54yerdgtfhjkuio98")
    # Comprobamos que trabajamos con una url en formato string y con una longitud igual o mayor a un caracter
    if type(webCrawler) != str or len(webCrawler) < 1:
        return False
    else:
        pass
    # Nos aseguramos que el link contenga el protocolo "https"
    if webCrawler.find('https') == -1:
        webCrawler = cabecera + webCrawler
    else:
        pass
    # Recogemos el contenido de la url y lo guardamos en una variable
    r = requests.get(webCrawler)
    # Comprobamos que la información recogida no coincide con la información que muestra la página web cuando devuelve error al tratar de localizar el link
    codigoWeb = r.text
    if codigoWeb == inexistent.text:
        return False
    return codigoWeb


def obtenerDatos(codigo):
    # Obtenemos los campos de la nave
    modelo = codigo[codigo.find("<h3>") + 4: codigo.find(" - ")]
    marca = codigo[codigo.find(" - ") + 3: codigo.find("</h3>")]
    gama = codigo[codigo.find("<p>Gama:") + 9: codigo.find(" (Tasa")]
    tasa = int(codigo[codigo.find("(Tasa:") + 7: codigo.find("§")])
    # Arreglamos el codigo para buscar color
    codigo = codigo[codigo.find("<p>Color:"):]
    color = codigo[codigo.find(
        "<p>Color:") + 10: codigo[codigo.find("<p>Color:"):].find("</p>")]
    plazas = int(
        codigo[codigo.find("<h2>Numero de plazas: <b>") + 25: codigo.find("</b>")])
    # Arreglamos el codigo para buscar las caracteristicas
    codigo = codigo[codigo.find("<div class=\"caracteristicas\">") + 29:]
    caracteristicas = []
    # Creamos un loop que guarda las caracteristicas de la nave en una lista
    while codigo.count("<p>") != 0:
        caracteristicas.append(
            codigo[codigo.find("<p>") + 3: codigo.find("</p>")])
        codigo = codigo[codigo.find("</p>") + 4:]
    nave = {'modelo': modelo, 'marca': marca, 'gama': gama, 'tasa': tasa,
            'color': color, 'plazas': plazas, 'caracteristicas': caracteristicas}
    return nave


def getLinks(url):
    # Creamos una variable para el link, los enlaces que recogeremos del correspondiente link y los links que queremos evitar recoger
    codigo = url

    if url == -1:
        codigo = obtenerCodigo(url)
    listaLinks = []
    listaProhibidos = ["./index.html", "../index.html",
                       "./contacto.html", "../contacto.html", "baja.html", "media.html", "alta.html"]
    # Buscamos la posición de los enlaces dentro del código web en formato string
    while True:
        inicio_href = codigo.find("href=")
        inicio_url = codigo.find('"', inicio_href)
        fin_url = codigo.find('"', inicio_url + 1)
        # Comprobamos que podemos trabajar con el codigo de la url
        if len(codigo) == 0:
            break
        elif inicio_href == -1:
            break
        # Buscamos los enlaces, nos aseguramos de que no pertenecen a la lista de link prohibidos y en ese caso los añadimos a la lista de links
        # Recortamos el codigo con el que trabajamos desde la última posición de cada link
        else:
            link = codigo[inicio_url + 1: fin_url]
            if link.find("html") == -1:
                codigo = codigo[fin_url:]
            elif link in listaProhibidos:
                codigo = codigo[fin_url:]
            else:
                listaLinks.append(codigo[inicio_url + 1: fin_url])
                codigo = codigo[fin_url:]
    return listaLinks


def union(p, q):
    # Recogemos la lista de links de la función getLinks y recogemos la lista de toCrawl de la función webCrawler
    # Nos aseguramos de que estamos trabajando con listas en ambos casos
    if type(p) != list or type(q) != list:
        return False
    # Seleccionamos cada link individualmente de la lista de listLinks de la función getLinks
    for e in q:
        # En el caso de que el link no se encuntre dentro de la lista de toCrawl lo añadimos y en caso contrario pasamos al siguiente link
        if e not in p:
            p.append(e)
    return p


def webCrawler(seed):
    # Creamos tres variables que tendrán el valor de tres listas distintas, en bannedLinks hemos añadido los links con los cuales no nos interesa trabajar, en toCrawl los links que aún falta para crawlear y en crawled los links que yahan sido crawleados
    banedLinks = [seed, "https://proyectodual.000webhostapp.com/",
                  "./catalogo.html", "../catalogo.html"]
    toCrawl = [seed]
    crawled = []
    # Creamos un bucle que funcionará mientras toCrawl no esté vacia, y eliminamos el último link de la lista que tendrá el valor de la variable "page"
    while toCrawl:
        page = toCrawl.pop()
        # Comprobamos que el valor de la variable page no se encuntre dentro de la lista de los links ya crawleados, en el caso de que no se encuentre, invocaremos al resto de funciones
        if page not in crawled:
            union(toCrawl, getLinks(obtenerCodigo(page)))
            crawled.append(page)
    # Creamos otro link que recogera uno a uno los links que se encuentran dentro de la lista de crawleados y buscaremos la información para la cual ha sido dieseñado este programa de web scraping
    for link in crawled:
        if link not in banedLinks:
            insertarUno(obtenerDatos(obtenerCodigo(link)))
        else:
            pass
    return crawled
