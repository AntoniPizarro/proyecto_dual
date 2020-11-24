import requests


def obtenerCodigo(webCrawler):
    inexistent = requests.get(
        "https://proyectodual.000webhostapp.com/1981781ji98p7654yrtgfhjkliop897i6u54yerdgtfhjkuio98")
    if type(webCrawler) != str or len(webCrawler) < 1:
        return False
    cabecera = "https://proyectodual.000webhostapp.com/"
    if webCrawler.find('https') == -1:
        webCrawler = cabecera + webCrawler
    r = requests.get(webCrawler)
    codigoWeb = r.text
    if codigoWeb == inexistent.text:
        return False
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
    return crawled
