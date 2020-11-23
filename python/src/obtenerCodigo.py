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
