"""
Создать список из словарей с оценками учеников разных классов школы
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.
"""

school = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]}, {'school_class': '9b', 'scores': [3, 3, 3, 4, 2]},
          {'school_class': '2b', 'scores': [5, 4, 2, 5, 3]}]

print("Средний бал по классу:")
for i in school:
    print(i["school_class"], "-", sum(i for i in i["scores"]) / len(i["scores"]))  # средний бал по классу
print("Средний бал по школе:")
a = []
for i in school:
    s = (i["scores"])
    a.append(s)
print((sum(map(sum, a))) / (sum(map(len, a))))
