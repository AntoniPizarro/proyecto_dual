from src.scrappingLinks import scrappingLinks
import pytest

# pytest -v test/scrappingLinks.py


# AQUI LOS CASOS TEST


def test_webCrawler():
    assert webCrawler("https://proyectodual.000webhostapp.com/") == [
        'https://proyectodual.000webhostapp./', './contacto.html', './catalogo.html', 'baja.html', 'media.html', 'alta.html', './index.html']
