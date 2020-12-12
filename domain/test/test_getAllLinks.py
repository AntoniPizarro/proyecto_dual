from src.scrappingLinks import getLinks, obtenerCodigo
import pytest

# pytest -v test/test_getAllLinks.py


def test_linksOtraPaginaWebIndex():
    assert getLinks(obtenerCodigo("https://paulk123.000webhostapp.com/")) == [
        'Free_Lily.html', 'movie_rank.html', 'videos.html', 'audios.html']


def test_linksOtraPaginaWebMovieRank():
    assert getLinks(obtenerCodigo("https://paulk123.000webhostapp.com/movie_rank.html")
                    ) == ['Free_Lily.html', 'movie_rank.html', 'videos.html', 'audios.html']


@pytest.mark.enlacesIndex
def test_IndexLinks():
    assert getLinks(obtenerCodigo("https://proyectodual.000webhostapp.com/")
                    ) == ["./catalogo.html"]


def test_contactosLinks():
    assert getLinks(obtenerCodigo("https://proyectodual.000webhostapp.com/contacto.html")
                    ) == ['./catalogo.html']


def test_NaveLinks():
    assert getLinks(obtenerCodigo(
        "https://proyectodual.000webhostapp.com/transports/y-wing.html")) == ['../catalogo.html']


def test_CatalogoLinks():
    assert getLinks(obtenerCodigo("https://proyectodual.000webhostapp.com/catalogo.html")) == ['./catalogo.html', 'transports/y-wing.html', 'transports/t70-xwing.html', 'transports/magna-guard.html', 'transports/neimoidian-escort.html',
                                                                                               'transports/cañonera-republica.html', 'transports/twilight.html', 'transports/aa-9.html', 'transports/crucero-alderaan.html', 'transports/gr-75.html', 'transports/imperial-shuttle.html', 'transports/v-wing.html']


"""
[
E            './index.html',
E            './catalogo.html',
E            './contacto.html',
E            'alta.html',
E            'media.html',
E            'baja.html',
E         -  'transports/y-wing.html',
E         -  'transports/t70-xwing.html',
E         -  'transports/magna-guard.html',
E         -  'transports/neimoidian-escort.html',
E         -  'transports/cañonera-republica.html',
E         -  'transports/twilight.html',
E         -  'transports/aa-9.html',
E         -  'transports/crucero-alderaan.html',
E         -  'transports/gr-75.html',
E         -  'transports/imperial-shuttle.html',
E         -  'transports/v-wing.html',
E           ]

"""
