class Stationery:

    def __init__(self, title): # атрибут
        self.title = title

    def draw(self):
        return f'запуск отрисовки {self.title}'



class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'вы взяли {self.title}. запуск отрисовки ручкой'


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'вы взяли {self.title}!? запуск отрисовки карандашом'


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'вы взяли {self.title}? запуск отрисовки маркером'

pen = Pen('Ручку')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())