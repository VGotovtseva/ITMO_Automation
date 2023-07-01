def task_one(a: int, b: int) -> int:
    if a > b:
        return a
    else:
        return b


print(task_one(5, 28))

def task_two(c: int, d: int):
    if (c > d and abs(c - d) == 135) or (d > c and abs(d - c) == 135):
        print("yes")
    else:
        print("no")


task_two(0, -135)

def task_three(month_number: int):
    if month_number in (1, 2, 12):
        print("зима")
    elif month_number in (3, 4, 5):
        print("весна")
    elif month_number in (6, 7, 8):
        print("лето")
    elif month_number in (9, 10, 11):
        print("осень")
    else:
        print("Введите число от 1 до 12")


task_three(7)


def task_four(e: int, f: int, j: int):
    if e > 10 and f > 10 and j > 10:
        print("yes")
    else:
        print("no")


task_four(11, -2, 14)


def task_five(list1: list) -> int:
    summa = 0
    for elem in list1:
        if elem > 0:
            summa += 1
    return summa


print(task_five([1, 2, -1, 3, 0]))


def task_six(years: int, month: int):
    if years >= 0 and month >= 0:
        days = (years * 12 * 29) + (month * 29)
        print(days)
    else:
        print("Введите год и месяц больше 0")


task_six(2, 10)


