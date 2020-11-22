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
