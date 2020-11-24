# Obtener codigo html

import requests

# insertarUno(obtenerDatos(obtenerCodigo("https://proyectodual.000webhostapp.com/transports/y-wing.html")))


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
            else:
                listaLinks.append(codigo[inicio_url + 1: fin_url])
                codigo = codigo[fin_url:]
    print(listaLinks)
    return listaLinks


def union(p, q):
    if type(p) != list or type(q) != list:
        return False
    for e in q:
        if e not in p:
            p.append(e)
    return p


def webCrawler(seed):
    toCrawl = [seed]
    crawled = []
    while toCrawl:
        page = toCrawl.pop()
        if page not in crawled:
            union(toCrawl, getLinks(obtenerCodigo(page)))
            crawled.append(page)
    print(crawled)
    return crawled


if __name__ == "__main__":

    # assert union(["a", "b", "d", "g", "h"], ["a", "b", "c", "d", "e", "f", "g", "h", "i"]) == ["a", "b", "d", "g", "h", "c", "e", "f", "i"]
    # assert webCrawler("https://proyectodual.000webhostapp.com/") == ['https://proyectodual.000webhostapp.com/', './contacto.html', './catalogo.html', 'transports/v-wing.html', '../contacto.html', '../catalogo.html', '../index.html', 'transports/imperial-shuttle.html', 'transports/gr-75.html','transports/crucero-alderaan.html', 'transports/aa-9.html', 'transports/twilight.html', 'transports/cañonera-republica.html', 'transports/neimoidian-escort.html', 'transports/magna-guard.html', 'transports/t70-xwing.html', 'transports/y-wing.html', 'baja.html', 'media.html', 'alta.html', './index.html']
    # assert webCrawler("https://paulk123.000webhostapp.com/") == ['https://paulk123.000webhostapp.com/', 'audios.html', 'videos.html', 'movie_rank.html', 'Free_Lily.html']

    # assert getLinks(obtenerCodigo("https://proyectodual.000webhostapp.com/")) == ["./index.html", "./catalogo.html", "./contacto.html"]

    # assert getLinks(obtenerCodigo("https://proyectodual.000webhostapp.com/catalogo.html")) == ['./index.html', './catalogo.html', './contacto.html', 'alta.html', 'media.html', 'baja.html', 'transports/y-wing.html','transports/t70-xwing.html', 'transports/magna-guard.html', 'transports/neimoidian-escort.html', 'transports/cañonera-republica.html', 'transports/twilight.html', 'transports/aa-9.html', 'transports/crucero-alderaan.html', 'transports/gr-75.html', 'transports/imperial-shuttle.html', 'transports/v-wing.html']
    # assert getLinks(obtenerCodigo("https://proyectodual.000webhostapp.com/contacto.html")) == ['./index.html', './catalogo.html', './contacto.html']
    #assert getLinks(obtenerCodigo("https://paulk123.000webhostapp.com/")) == ['Free_Lily.html', 'movie_rank.html', 'videos.html', 'audios.html', 'test-html.html']
    #assert getLinks(obtenerCodigo("https://proyectodual.000webhostapp.com/transports/y-wing.html")) == ['../index.html', '../catalogo.html', '../contacto.html']
    assert getLinks(obtenerCodigo(
        "https://paulk123.000webhostapp.com/movie_rank.html")) == ['Free_Lily.html', 'movie_rank.html', 'videos.html', 'audios.html']
