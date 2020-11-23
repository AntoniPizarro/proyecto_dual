from src.scrappingLinks import webCrawler
import pytest

# pytest -v test/scrappingLinks.py


# AQUI LOS CASOS TEST


def test_webCrawler():
    assert webCrawler("https://proyectodual.000webhostapp.com/") == ['https://proyectodual.000webhostapp.com/', './contacto.html', './catalogo.html', 'transports/v-wing.html', '../contacto.html', '../catalogo.html', '../index.html', 'transports/imperial-shuttle.html', 'transports/gr-75.html',
                                                                     'transports/crucero-alderaan.html', 'transports/aa-9.html', 'transports/twilight.html', 'transports/cañonera-republica.html', 'transports/neimoidian-escort.html', 'transports/magna-guard.html', 'transports/t70-xwing.html', 'transports/y-wing.html', 'baja.html', 'media.html', 'alta.html', './index.html']
