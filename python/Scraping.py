# Obtener codigo html

import requests


def obtenerCodigo(url):
    if len(url) < 1 or type(url) != str:
        return False
    cabecera = "https://paulk123.000webhostapp.com/"
    if url.find('https') == -1:
        url = cabecera + url
    r = requests.get(url)
    codigoWeb = r.text
    return codigoWeb
    
def crawler(url):
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


if __name__ == "__main__":
    assert crawler("https://paulk123.000webhostapp.com/") == ["Free_Lily.html","movie_rank.html","videos.html","audios.html"]



