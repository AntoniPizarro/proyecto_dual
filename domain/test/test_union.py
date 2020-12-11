from src.scrappingLinks import union
import pytest

# pytest -v test/test_union.py


def test_dosArrays():
    assert union(["a", "b", "d", "g", "h"], ["a", "b", "c", "d", "e", "f", "g", "h", "i"]) == [
        "a", "b", "d", "g", "h", "c", "e", "f", "i"]


def test_unValorNoArray():
    assert union("aaaaa", ["a", "b", "c", "d",
                           "e", "f", "g", "h", "i"]) == False


def test_dosValoresNoArray():
    assert union("aaaaa", "idrb") == False


def test_unValorIntegros():
    assert union(["a", "b", "c"], 156848) == False


def test_unValorIntegroUnValorString():
    assert union(123432, "estoesunastring") == False


def test_arraysIntegros():
    assert union([1, 2, 3, 4], [1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
