# Obtener codigo html

import requests


def obtenerCodigo(webCrawler):
    if len(webCrawler) < 1 or type(webCrawler) != str:
        return False
    cabecera = "https://proyectodual.000webhostapp.com/"
    if webCrawler.find('https') == -1:
        webCrawler = cabecera + webCrawler
    r = requests.get(webCrawler)
    codigoWeb = r.text
    return codigoWeb


def getLinks(url):
    codigo = url
    if url == -1:
        codigo = obtenerCodigo(url)
    listaLinks = []
    while True:
        inicio_href = codigo.find("<a href=")
        inicio_url = codigo.find('"', inicio_href)
        fin_url = codigo.find('"', inicio_url + 1)
        if len(codigo) == 0:
            break
        elif inicio_href == -1:
            break
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
    #assert webCrawler("https://proyectodual.000webhostapp.com/") == ['https://proyectodual.000webhostapp.com/', './contacto.html', './catalogo.html', 'baja.html', 'media.html', 'alta.html', './index.html']
    assert webCrawler("https://paulk123.000webhostapp.com/") == [
        'https://paulk123.000webhostapp.com/', 'audios.html', 'videos.html', 'movie_rank.html', 'Free_Lily.html']


"""
def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled

"""
