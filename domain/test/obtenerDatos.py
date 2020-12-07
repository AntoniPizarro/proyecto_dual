from src.scrappingLinks import obtenerDatos, obtenerCodigo
import pytest

# pytest -v test/obtenerDatos.py


def test_yWing():
    assert obtenerDatos(obtenerCodigo("https://proyectodual.000webhostapp.com/transports/y-wing.html")) == {
        'modelo': "Y-Wing", 'marca': "República", 'gama': "Baja", 'tasa': 15, 'color': "Blanco", 'plazas': 2, 'caracteristicas': ["Torpedos", "Hipervelocidad", "Cabina"]}


def test_vWing():
    assert obtenerDatos(obtenerCodigo("https://proyectodual.000webhostapp.com/transports/v-wing.html")) == {
        'modelo': "V-Wing", 'marca': "República", 'gama': "Baja", 'tasa': 15, 'color': "Blanco", 'plazas': 1, 'caracteristicas': ["Torpedos", "Cabina", "Hipervelocidad"]}


def test_neimoidianEscortShuttle():
    assert obtenerDatos(obtenerCodigo("https://proyectodual.000webhostapp.com/transports/neimoidian-escort.html")) == {
        'modelo': "Neimoidian Escort Shuttle", 'marca': "CSI", 'gama': "Media", 'tasa': 25, 'color': "Gris", 'plazas': 4, 'caracteristicas': ["Escudos", "Hipervelocidad", "Patas extensibles", "Puente de mando"]}


def test_cañoneraRepublica():
    assert obtenerDatos(obtenerCodigo("https://proyectodual.000webhostapp.com/transports/ca%C3%B1onera-republica.html")) == {
        'modelo': "Cañonera de la República", 'marca': "República", 'gama': "Media", 'tasa': 25, 'color': "Blanco", 'plazas': 6, 'caracteristicas': ["Cañones de iones", "Misileros", "Cabina", "Camara de carga"]}


def test_cruceroAldearaan():
    assert obtenerDatos(obtenerCodigo("https://proyectodual.000webhostapp.com/transports/crucero-alderaan.html")) == {
        'modelo': "Crucero de Alderaan", 'marca': "Rebelión", 'gama': "Alta", 'tasa': 50, 'color': "Blanco", 'plazas': 20, 'caracteristicas': ["Escudos", "Turbo laser", "Hipervelocidad", "Puerto", "Puente de mando"]}


def test_imperialShuttle():
    assert obtenerDatos(obtenerCodigo("https://proyectodual.000webhostapp.com/transports/imperial-shuttle.html")) == {
        'modelo': "Imperial Shuttle", 'marca': "Imperio Galáctico", 'gama': "Alta", 'tasa': 50, 'color': "Gris", 'plazas': 6, 'caracteristicas': ["Cañones de iones", "Escudos", "Hipervelocidad", "Patas extensibles", "Puente de mando"]}
