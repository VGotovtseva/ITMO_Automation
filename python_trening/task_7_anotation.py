a: int = 5
b: str = 'строка'
с: list = [1, 2]


def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s


print(indent('123', 123))

# можно указать возвращаемое значение после стрелки и завершающего двоеточия, если ничего не возвращает -> none:
# возврат по разным условиям () -> None or str:

def len_str(s: str ='') -> int:
    return len(s)


print(len_str('Hello world!'))


def max_len(a: list, b: list) -> int:
    return max(len(a), len(b))


print(max_len([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4]))


def func_list(list1: list, v) -> list:
    list1.append(v)
    return list1


print(func_list([1, '2', 1.24], 'шесть'))



def func_list2(list2: list) -> int:

#return sum(list2) - первое решение
   summa = 0
   for elem in list2:
       summa = summa + elem
   return summa


print(func_list2([1, 2, 3, 4]))
