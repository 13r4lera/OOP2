
class Fraction:
    def __init__(self, integer=0, fractional="0"):
        text = str(fractional)
        digits = text.removeprefix("-")

        if type(integer) is not int or not digits.isdigit():
            raise ValueError("Введите целые числа")
        if integer > 0 and text.startswith("-"):
            raise ValueError("Знаки частей должны совпадать")

        self.integer = integer
        self.fractional = int(digits)
        if integer < 0 or text.startswith("-"):
            self.fractional = -self.fractional
        self.places = len(digits)

    def read(self):
        integer = int(input("Целая часть: "))
        fractional = input("Дробная часть: ")
        self.__init__(integer, fractional)

    def display(self):
        number = self._value(self.places)
        sign = "-" if number < 0 else ""
        digits = str(abs(self.fractional)).zfill(self.places).rstrip("0") or "0"
        print(f"{sign}{abs(self.integer)},{digits}")

    def _value(self, places):
        number = self.integer * 10**self.places + self.fractional
        return number * 10 ** (places - self.places)

    def _make(self, number, places):
        result = Fraction()
        sign = -1 if number < 0 else 1
        result.integer = sign * (abs(number) // 10**places)
        result.fractional = sign * (abs(number) % 10**places)
        result.places = places
        return result

    def __add__(self, other):
        places = max(self.places, other.places)
        return self._make(self._value(places) + other._value(places), places)

    def __sub__(self, other):
        places = max(self.places, other.places)
        return self._make(self._value(places) - other._value(places), places)

    def __mul__(self, other):
        places = self.places + other.places
        return self._make(self._value(self.places) * other._value(other.places), places)

    def __eq__(self, other):
        places = max(self.places, other.places)
        return self._value(places) == other._value(places)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        places = max(self.places, other.places)
        return self._value(places) < other._value(places)

    def __gt__(self, other):
        return other < self

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other


if __name__ == "__main__":
    a = Fraction(1, 50)
    b = Fraction(2, 25)

    print("a =", end=" ")
    a.display()
    print("b =", end=" ")
    b.display()
    print("a + b =", end=" ")
    (a + b).display()
    print("a - b =", end=" ")
    (a - b).display()
    print("a * b =", end=" ")
    (a * b).display()

    print("a == b:", a == b)
    print("a != b:", a != b)
    print("a < b:", a < b)
    print("a > b:", a > b)
    print("a <= b:", a <= b)
    print("a >= b:", a >= b)

    c = Fraction()
    c.read()
    print("Введено:", end=" ")
    c.display()
