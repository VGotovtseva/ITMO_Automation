class Soda:

    def __init__(self, adds=''):

        self.adds = adds
    def show_my_drink(self):
        if self.adds:
            print(f"Газировка и {self.adds}")
        else:
           print("Обычная газировка")

fanta = Soda('апельсин')
sprite = Soda()

fanta.show_my_drink()
sprite.show_my_drink()