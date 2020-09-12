"""''
Написать функцию, которая принимает на вход две строки
Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
Если строки одинаковые, вернуть 1
Если строки разные и первая длиннее, вернуть 2
Если строки разные и вторая строка 'learn', возвращает 3
''"""


def check(edit_line, edit_line1):
    if edit_line == edit_line1:
        return 1  # строки одинаковые
    elif len(edit_line) > len(edit_line1):
        return 2  # первая строка больше второй
    elif edit_line != edit_line1 and edit_line1 == 'learn':
        return 3
    elif type(edit_line) and type(edit_line1) != str:
        return 0


print("Введите первую строку:")
edit_line = input()
print("Ведите вторую строк:")
edit_line1 = input()

print(check(edit_line, edit_line1))
