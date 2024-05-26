import json
from konwersja import Konwerter
import pytest
import requests

@pytest.fixture()
def konwerter_f(monkeypatch):
    def moj_get(*args, **kwargs):
        class Resp:
            def json(self, *args, **kwargs):
                with open('kursy.json') as f:
                    j = json.load(f)
                return j
        return Resp()
    monkeypatch.setattr(requests, 'get', moj_get)
    return Konwerter()


@pytest.fixture(scope='session')
def dane_test():
    with open('dane_kursy.json') as f:
        return json.load(f)


def test_ok(konwerter_f, dane_test):
    for args, wynik in dane_test:
        assert konwerter_f.konwertuj(*args) == pytest.approx(wynik)

def test_ok_monkeypatch(konwerter_f, dane_test):

    for args, wynik in dane_test:
        assert konwerter_f.konwertuj(*args) == pytest.approx(wynik)
