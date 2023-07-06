from task_9_checks import Checks


class Input(Checks):

    def __init__(self, loc):
        super().__init__(loc)


search = Input('произвольное значение')
print(search.check_text())

class Button(Checks):

    def __init__(self, loc):
        super().__init__(loc)


search_two = Button('произвольное значение 2')
print(search_two.check_text())


class Title(Checks):

    def __init__(self, loc):
        super().__init__(loc)


search_three = Title('произвольное значение 3')
print(search_three.check_text())


class Link(Checks):

    def __init__(self, loc):
        super().__init__(loc)


search_four = Link('произвольное значение 4')
print(search_four.check_text())



