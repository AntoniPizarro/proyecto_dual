# Obtener codigo html

import requests
from repository.PythonToMongo import insertarUno

# insertarUno(obtenerDatos(obtenerCodigo("https://proyectodual.000webhostapp.com/transports/y-wing.html")))


def obtenerCodigo(url):
    if len(url) < 1 or type(url) != str:
        return False
    cabecera = "https://proyectodual.000webhostapp.com/"
    if url.find('https') == -1:
        url = cabecera + url
    r = requests.get(url)
    url = r.text
    return url


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
    codigo = url
    if url == -1:
        codigo = obtenerCodigo(url)
    listaLinks = []
    listaProhibidos = ["./index.html", "../index.html",
                       "./contacto.html", "../contacto.html", "baja.html", "media.html", "alta.html"]
    while True:
        inicio_href = codigo.find("href=")
        inicio_url = codigo.find('"', inicio_href)
        fin_url = codigo.find('"', inicio_url + 1)
        if len(codigo) == 0:
            break
        elif inicio_href == -1:
            break
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
    if type(p) != list or type(q) != list:
        return False
    for e in q:
        if e not in p:
            p.append(e)
    return p


def webCrawler(seed):
    banedLinks = [seed,
                  "./catalogo.html", "../catalogo.html"]
    toCrawl = [seed]
    crawled = []
    while toCrawl:
        page = toCrawl.pop()
        if page not in crawled:
            union(toCrawl, getLinks(obtenerCodigo(page)))
            crawled.append(page)
    for link in crawled:
        if link not in banedLinks:
            insertarUno(obtenerDatos(obtenerCodigo(link)))
        else:
            pass
    return crawled