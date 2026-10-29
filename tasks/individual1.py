import math
import sys


class Pair:
    def __init__(self, first, second):
        if isinstance(first, (int, float)) and isinstance(second, (int, float)):
            self.first = float(first)
            self.second = float(second)
        else:
            raise TypeError

    def read(self):
        self.first = float(input("Введите координату first: "))
        self.second = float(input("Введите координату second: "))

    def display(self):
        print(f"first = {self.first}, second = {self.second}")

    def distance(self):
        return math.sqrt(self.first ** 2 + self.second ** 2)


def make_pair(first, second):
    if isinstance(first, (int, float)) and isinstance(second, (int, float)):
        return Pair(first, second)
    else:
        print("Ошибка: параметры должны быть числами!")
        sys.exit()


if __name__ == '__main__':
    p1 = make_pair(3, 4)
    p1.display()
    print(f"Расстояние: {p1.distance()}")

    p2 = Pair(0, 0)
    p2.read()
    p2.display()
    print(f"Расстояние: {p2.distance()}")

    p3 = make_pair("abc", 5)