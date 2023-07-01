def task_1() -> int or float or str or bool or list:
    a: int = 2
    b: float = 1.25
    c: str = 'привет'
    d: list = [1, 2, 3, 4]
    e: bool = True
    return type(a), type(b), type(c), type(d), type(e)


print(task_1())

def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]

print(task_2())

#эта последовательность чисел называется Числа Фибоначчи, где каждое число - сумма двух предыдущих чисел из списка


def task_3(a: int) -> int:
    return pow(a, 2)


print(task_3(3))




