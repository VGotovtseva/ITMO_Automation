class Input:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search = Input('произвольное значение', 'Поиск')

class Button:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search_two = Button('произвольное значение 2', 'Поиск 2')

class Title:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search_three = Title('произвольное значение 3', 'Поиск 3')

class Link:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search_four = Link('произвольное значение 4', 'Поиск 4')


print(search.loc, search.text)
print(search_two.loc, search_two.text)
print(search_three.loc, search_three.text)
print(search_four.loc, search_four.text)
