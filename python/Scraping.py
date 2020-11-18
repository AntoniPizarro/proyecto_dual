# Obtener codigo html

import requests

def obtenerCodigo(url):
    r = requests.get(url)
    codigoWeb = r.text
    print(codigoWeb)