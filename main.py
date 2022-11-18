'''
Домашнє завдання
1. Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії
 із зазначеним множником.
 Генератор повинен зупинити свою роботу або після досягнення зазначеного елементу,
 або при передачі команди на завершення.
2. Реалізуйте свій аналог генераторної функції range().
3. Напишіть функцію-генератор, яка повертатиме прості числа.
 Верхня межа діапазону повинна бути задана параметром цієї функції.
4. Напишіть генераторний вираз для заповнення списку.
 Список повинен бути заповнений кубами чисел від 2 до вказаної вами величини.
'''

from my_range import MyRange

VALUE_LIMIT = 10_000

def prime_numbers(lim:int=10):
    if not isinstance(lim, int):
        raise ValueError
    for i in range(2, lim + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i

def geometric_progression(multiplier):
    is_it_end = False
    res = 1
    while not is_it_end:
        send_ = yield res
        if send_ is not None:
            return
        res = res * multiplier


def main():
    # 1)
    # g = geometric_progression(2)
    # for item in g:
    #     user_input = input(f"Value = {item}, press 'N' to end").lower()
    #     if user_input == 'n':
    #         try:
    #             g.send(user_input)
    #         except StopIteration:
    #             pass
    #     if item > VALUE_LIMIT:
    #         g.close()

    # 2)
    # mr = MyRange()
    # for i in mr.range(6):
    #     print(i)
    # for i in mr.range(7, 10):
    #     print(i)
    # for i in mr.range(2, 16, 3):
    #     print(i)

    # 3)
    print(*prime_numbers(1000))





if __name__ == "__main__":
    main()
