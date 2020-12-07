from src.area_esfera import areaEsfera
import pytest

# pytest -v test/area_esfera.py


# AQUI LOS CASOS TEST


def test_areaEsfera():
    assert areaEsfera(10) == 1256.6370614359173
