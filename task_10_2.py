from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
    def __init__(self, size: float):
        self.size = size

    @property
    def calculate(self):
        return round(self.size / 6.5 + 0.5, 2)


class Costume(Clothes):
    def __init__(self, height: float):
        self.height = height

    @property
    def calculate(self):
        return round(2 * self.height + 0.3, 2)


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)
    print(costume.calculate)