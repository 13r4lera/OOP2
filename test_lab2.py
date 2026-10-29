
from tasks.individual1 import Pair
from tasks.individual2 import Fraction


def test_pair():
    assert Pair(3, 4).distance() == 5


def test_add():
    assert Fraction(1, 50) + Fraction(2, 25) == Fraction(3, 75)


def test_sub():
    assert Fraction(1, 50) - Fraction(2, 25) == Fraction(0, "-75")


def test_mul():
    assert Fraction(1, 50) * Fraction(2, 25) == Fraction(3, 375)


def test_compare():
    a = Fraction(1, 50)
    b = Fraction(2, 25)
    assert a < b and a <= b and b > a and b >= a
    assert a != b and a == Fraction(1, 5)


def test_many_digits():
    a = Fraction(0, "00000000000000000001")
    b = Fraction(0, "00000000000000000002")
    assert a + b == Fraction(0, "00000000000000000003")


def test_exact_multiplication():
    a = Fraction(0, "00000000001")
    assert a * a == Fraction(0, "0000000000000000000001")


def test_negative():
    assert Fraction(0, "05") - Fraction(0, "10") == Fraction(0, "-05")
