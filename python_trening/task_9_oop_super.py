class A:

    def __init__(self):
        self.x = 10

class B(A):
    def __init__(self):
        super().__init__()
        self.y = self.x + 5


print(B().y)

b = B()
print(b.y)



class BasePage:
    def __init__(self, base_url):
        self.base_url = base_url

    def visit(self):
        return f"Выполнен вход по урлу {self.base_url}"

class HomePage(BasePage):
    def __init__(self, base_url): # в данном случае нет необходимости инициализировать base_url еще раз,
        # тк у нас есть доступ к этому атрибуту от наследуемого класса
        super().__init__(base_url)


main = HomePage("https://main.ru")
print(main.visit())
