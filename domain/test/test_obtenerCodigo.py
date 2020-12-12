from src.scrappingLinks import obtenerCodigo
import pytest
import requests

# pytest -v test/test_obtenerCodigo.py


@pytest.mark.codigoIndex
def test_obtenerElMismoCodigo():
    assert obtenerCodigo("https://proyectodual.000webhostapp.com/") == requests.get(
        "https://proyectodual.000webhostapp.com/").text


def test_integros():
    assert obtenerCodigo(123) == False


def test_stringVacia():
    assert obtenerCodigo("") == False


def test_urlFalsa():
    assert obtenerCodigo("fghjkjytrfghjkiuygfcvbnmj") == False


def test_array():
    assert obtenerCodigo(["asda", "tesco", "sainsbury"]) == False


def test_stringSimple():
    assert obtenerCodigo("hola") == False
