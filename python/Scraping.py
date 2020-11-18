# Obtener codigo html

import requests


def obtenerCodigo(url):
    if url.find('https') == -1:
        url = "https://paulk123.000webhostapp.com/" + url
    r = requests.get(url)
    codigoWeb = r.text
    print(codigoWeb)
