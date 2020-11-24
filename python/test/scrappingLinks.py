from src.scrappingLinks import webCrawler
import pytest

# pytest -v test/scrappingLinks.py


# AQUI LOS CASOS TEST


def test_webCrawler():
    assert webCrawler("https://proyectodual.000webhostapp.com/") == ['./index.html', './catalogo.html', './contacto.html', 'alta.html', 'media.html', 'baja.html', 'transports/y-wing.html',
                                                                     'transports/t70-xwing.html', 'transports/magna-guard.html', 'transports/neimoidian-escort.html', 'transports/cañonera-republica.html', 'transports/twilight.html', 'transports/aa-9.html', 'transports/crucero-alderaan.html', 'transports/gr-75.html', 'transports/imperial-shuttle.html', 'transports/v-wing.html']
