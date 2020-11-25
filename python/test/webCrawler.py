from src.scrappingLinks import webCrawler
import pytest

# pytest -v test/webCrawler.py

# AQUI LOS CASOS TEST
# DESDE CADA UNO DE LOS ENLACES DE NUESTRA PÁGINA WEB


def test_indexWebPage():
    assert webCrawler("https://proyectodual.000webhostapp.com/index.html") == ['https://proyectodual.000webhostapp.com/index.html', './catalogo.html', 'transports/v-wing.html', '../catalogo.html', 'transports/imperial-shuttle.html', 'transports/gr-75.html',
                                                                               'transports/crucero-alderaan.html', 'transports/aa-9.html', 'transports/twilight.html', 'transports/cañonera-republica.html', 'transports/neimoidian-escort.html', 'transports/magna-guard.html', 'transports/t70-xwing.html', 'transports/y-wing.html']


def test_CatalogoWebPage():
    assert webCrawler("https://proyectodual.000webhostapp.com/catalogo.html") == ['https://proyectodual.000webhostapp.com/catalogo.html', 'transports/v-wing.html', "../catalogo.html", 'transports/imperial-shuttle.html', 'transports/gr-75.html', 'transports/crucero-alderaan.html', 'transports/aa-9.html',
                                                                                  'transports/twilight.html', 'transports/cañonera-republica.html', 'transports/neimoidian-escort.html', 'transports/magna-guard.html', 'transports/t70-xwing.html', 'transports/y-wing.html', './catalogo.html']


def test_contactoWebPage():
    assert webCrawler("https://proyectodual.000webhostapp.com/contacto.html") == ['https://proyectodual.000webhostapp.com/contacto.html', './catalogo.html', 'transports/v-wing.html', '../catalogo.html', 'transports/imperial-shuttle.html', 'transports/gr-75.html',
                                                                                  'transports/crucero-alderaan.html', 'transports/aa-9.html', 'transports/twilight.html', 'transports/cañonera-republica.html', 'transports/neimoidian-escort.html', 'transports/magna-guard.html', 'transports/t70-xwing.html', 'transports/y-wing.html']


def test_naveEjemplo():
    assert webCrawler("https://proyectodual.000webhostapp.com/transports/y-wing.html") == ['https://proyectodual.000webhostapp.com/transports/y-wing.html', '../catalogo.html', 'transports/v-wing.html', 'transports/imperial-shuttle.html', 'transports/gr-75.html',
                                                                                           'transports/crucero-alderaan.html', 'transports/aa-9.html', 'transports/twilight.html', 'transports/cañonera-republica.html', 'transports/neimoidian-escort.html', 'transports/magna-guard.html', 'transports/t70-xwing.html', 'transports/y-wing.html', './catalogo.html']
