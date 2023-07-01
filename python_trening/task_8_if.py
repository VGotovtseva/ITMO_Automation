num = 2


if num >= 0:
    print("Число больше либо равно 0")
else:
    print('Число отрицательное')


str_1 = "test"
str_2 = "test1"

if str_1 in str_2:
    print("ДА")
else:
    print('НЕТ')


num_float = -4.5


if num_float > 0:
    print("Положительное число")
elif num_float == 0:
    print("Ноль")
else:
    print("Число отрицательное")


permit_print = True


if num > 0 and permit_print:
    print("num - положительное число")
elif not permit_print:
    print("Печать запрещена")


def type_edu(a: int) -> str:
    if a >= 1 and a <= 4:
       print("Бакалавр")
    elif a>=5 and a <= 6: # a in (5,6) или range(5,7) в этой функции первое включительно, последнее не вкл-но
        print("Магистр")
    elif a >= 7 and a <= 9:
        print("Аспирант")
    else:
        print("Введите корректный курс обучения!")


type_edu(0)

def type_number(b: int) -> str:
    if b > 100 or b < -100:
        print("-")
    else:
        print("+")

type_number(100)



