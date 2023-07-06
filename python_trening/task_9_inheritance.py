class Mammal:
    className = 'Млекопитающее'

class Dog(Mammal): # наследование класса (должен быть в одном файле или добавлен импорт класса
    species = 'Canis lupus'

dog = Dog()
print(dog.className)

