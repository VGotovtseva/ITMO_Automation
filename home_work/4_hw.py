class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


one = Rectangle(3, 4)
two = Rectangle(1, 10)
three = Rectangle(2, 7)
print(f"Площадь первого прямоугольника: {one.square()}, периметр первого прямоугольника: {one.perimeter()}")
print(f"Площадь второго прямоугольника: {two.square()}, периметр второго прямоугольника: {two.perimeter()}")
print(f"Площадь третьего прямоугольника: {three.square()}, периметр третьего прямоугольника: {three.perimeter()}")

print("\n")

class Math:
    def __init__(self, a=6, b=2):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)


Math().addition()
Math().multiplication()
Math().division()
Math().subtraction()

print('\n')


class Button:

    type = 'Кнопка'

    def __init__(self, text, loc=''):
        self.text = text
        self.loc = loc

    def click(self):
        return f"Клик по кнопке {self.text}"


text_box = Button('Text_Box')
check_box = Button('Check_Box')
radio_button = Button('Radio_Button')
web_tables = Button('Web_Tables')
buttons = Button('Buttons')
links = Button('Links')
broken_links_images = Button('Broken_Links_Images')
upload_and_download = Button('Upload_AND_Download')
dynamic_properties = Button('Dynamic_Properties')


print(text_box.text)
print(text_box.click())

print(check_box.text)
print(check_box.click())

print(radio_button.text)
print(radio_button.click())

print(web_tables.text)
print(web_tables.click())

print(buttons.text)
print(buttons.click())

print(links.text)
print(links.click())

print(broken_links_images.text)
print(broken_links_images.click())

print(upload_and_download.text)
print(upload_and_download.click())

print(dynamic_properties.text)
print(dynamic_properties.click())