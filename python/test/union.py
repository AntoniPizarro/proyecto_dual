from src.scrappingLinks import union
import pytest

def test_dosArrays():
    assert union(["a","b","d","g","h"] , ["a","b","c","d","e","f","g","h","i"]) == ["a","b","d","g","h","c","e","f","i"]
def test_unValorNoArray():
    assert union("aaaaa" , ["a","b","c","d","e","f","g","h","i"]) == False
def test_dosValoresNoArray():
    assert union("aaaaa" , "idrb") == False