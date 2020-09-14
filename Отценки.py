"""
Создать список из словарей с оценками учеников разных классов школы
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.
"""

school = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]}, {'school_class': '9b', 'scores': [3, 3, 3, 4, 2]},
          {'school_class': '2b', 'scores': [5, 4, 2, 5, 3]}]

print("Средний бал по классу:")
for row in school:
    print(row["school_class"], sum(row["scores"])/len(row["scores"]))
print("Средний бал по всей школе:")
a = []
for line in school:
    for element in line["scores"]:
        a.append(element)
print(sum(a)/len(a))# средний бал по школе




