from src.scrappingLinks import getLinks, obtenerCodigo
import pytest

# pytest -v test/getAllLinks.py


def test_IndexLinks():
    assert getLinks(obtenerCodigo("https://proyectodual.000webhostapp.com/")
                    ) == ["./index.html", "./catalogo.html", "./contacto.html"]


def test_contactosLinks():
    assert getLinks(obtenerCodigo("https://proyectodual.000webhostapp.com/contacto.html")
                    ) == ['./index.html', './catalogo.html', './contacto.html']


def test_linksOtraPaginaWebIndex():
    assert getLinks(obtenerCodigo("https://paulk123.000webhostapp.com/")) == [
        'Free_Lily.html', 'movie_rank.html', 'videos.html', 'audios.html', 'test-html.html']


def test_linksOtraPaginaWebMovieRank():
    assert getLinks(obtenerCodigo("https://paulk123.000webhostapp.com/movie_rank.html")
                    ) == ['Free_Lily.html', 'movie_rank.html', 'videos.html', 'audios.html']


def test_linksNaveCatalogo():
    assert getLinks(obtenerCodigo(
        "https://proyectodual.000webhostapp.com/transports/y-wing.html")) == ['../index.html', '../catalogo.html', '../contacto.html']


def test_CatalogoLinks():
    assert getLinks(obtenerCodigo("https://proyectodual.000webhostapp.com/catalogo.html")) == ['./index.html', './catalogo.html', './contacto.html', 'alta.html', 'media.html', 'baja.html', 'transports/y-wing.html',
                                                                                               'transports/t70-xwing.html', 'transports/magna-guard.html', 'transports/neimoidian-escort.html', 'transports/cañonera-republica.html', 'transports/twilight.html', 'transports/aa-9.html', 'transports/crucero-alderaan.html', 'transports/gr-75.html', 'transports/imperial-shuttle.html', 'transports/v-wing.html']
