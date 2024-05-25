from wstep import dzielenie
import pytest

def test_dzielenie_ok():
    assert dzielenie(4, 2) == 2, '4 / 2 == 0'
    assert dzielenie(4, 1) == 4
    assert dzielenie(4, 8) == .5
    assert dzielenie(0, 2222) == 0
    assert dzielenie(-5, 2) == -2.5


def test_dzielenie_approx():
    assert dzielenie(4, 3) == pytest.approx(1.333333333)

def test_dzielenie_raises():
    with pytest.raises(ZeroDivisionError):
        dzielenie(5, 0)
    with pytest.raises(ZeroDivisionError):
        dzielenie(0, 0)
