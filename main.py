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
VALUE_LIMIT = 10_000


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
    g = geometric_progression(2)
    for item in g:
        user_input = input(f"Value = {item}, press 'N' to end").lower()
        if user_input == 'n':
            try:
                g.send(user_input)
            except StopIteration:
                pass
        if item > VALUE_LIMIT:
            g.close()

    # 2)


if __name__ == "__main__":
    main()
