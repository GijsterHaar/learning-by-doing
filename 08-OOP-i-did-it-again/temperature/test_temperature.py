
from temperature import Kelvin, Celcius

def test_create_kelvin():
    assert Kelvin(0)

def test_compare_kelvin():
    assert Kelvin(42) == Kelvin(42)

def test_add_kelvins():
    assert Kelvin(20) + Kelvin(30) == Kelvin(50)

def test_dividing_kelvin():
    assert Kelvin(100) // 2 == Kelvin(50)


def test_create_celcius():
    assert Celcius(0)

def test_compare_celcius():
    assert Celcius(20) == Celcius(20)


def test_comparing_celcius_kelvin():
    assert Celcius(0) == Kelvin(273)

def test_compare_kelvin_celcius():
    assert Kelvin(283) == Celcius(10)









# def test_add_celcius():
#     assert Celcius(20) + Celcius(20) == Celcius(40)

# def test_divide_celcius():
#     assert Celcius(100) // 4 == Celcius(25)