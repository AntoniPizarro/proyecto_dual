# Obtener codigo html

import requests

#insertarUno(obtenerDatos(obtenerCodigo("https://proyectodual.000webhostapp.com/transports/y-wing.html")))

def obtenerCodigo(webCrawler):
    if len(webCrawler) < 1 or type(webCrawler) != str:
        return False
    cabecera = "https://proyectodual.000webhostapp.com/"
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

def getLinks(url):
    codigo = url
    if url == -1:
        codigo = obtenerCodigo(url)
    listaLinks = []
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
                pass
                codigo = codigo[fin_url:]
            else:
                listaLinks.append(codigo[inicio_url + 1: fin_url])
                codigo = codigo[fin_url:]
    return listaLinks


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def webCrawler(seed):
    toCrawl = [seed]
    crawled = []
    while toCrawl:
        page = toCrawl.pop()
        if page not in crawled:
            union(toCrawl, getLinks(obtenerCodigo(page)))
            crawled.append(page)
    return crawled


if __name__ == "__main__":
    assert webCrawler("https://proyectodual.000webhostapp.com/") == ['https://proyectodual.000webhostapp.com/',
                                                                     './contacto.html', './catalogo.html', 'baja.html', 'media.html', 'alta.html', './index.html']
    #assert webCrawler("https://paulk123.000webhostapp.com/") == ['https://paulk123.000webhostapp.com/', 'audios.html', 'videos.html', 'movie_rank.html', 'Free_Lily.html']
