class Stationery:
    def __init__(self, title: str) -> None:
        self.title = title

    def draw(self) -> None:
        if self.__class__.__name__ == 'Pencil':
            print('Запуск отрисовки')
        print(f'{self.__class__.__name__}: приступил к отрисовке объекта "{self.title}"')

class Pen(Stationery):
    def function(self, function_object: str):
        self.function_object = function_object
        print(f'"{self.title}" имеет такую способность как: {function_object}')

class Pencil(Stationery):
    def function(self, function_object: str):
        self.function_object = function_object
        print(f'"{self.title}" имеет такую способность как: {function_object}')

class Handle(Stationery):
    def function(self, function_object: str):
        self.function_object = function_object
        print(f'"{self.title}" имеет такую способность как: {function_object}')


if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()  # Pen: приступил к отрисовке объекта "Ручка"
    handle.draw()  # Handle: приступил к отрисовке объекта "Маркер"
    pencil.draw()  # Пример вывода ниже в многострочном комментарии
    pencil.function('Стираемый') # "Карандаш" имеет такую способность как: Стираемый
