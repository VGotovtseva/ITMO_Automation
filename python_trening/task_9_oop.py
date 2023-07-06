class Button:  #создание класса,  его название с большой буквы

    def __init__(self, text, link): #метод инициализации, первый self (это внутренний объект класса через него
        # мы получаем к любому методу и атрибута класса)

        self.text = text
        self.link = link

# Создаем экземпляров класса - объектов


home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')


# Получаем доступ к атрибутам
print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)


print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)


class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

# создаем экземпляр класса


home_two = ButtonTwo('Домой', '/home', 'button#home')
one = ButtonTwo()

# вызываем метод
print(home_two.click())