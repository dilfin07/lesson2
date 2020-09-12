"""'' Перепишите функцию discounted(price, discount, max_discount=20)из урока про функции так, чтобы она
перехватывала исключения, когда переданы некорректные аргументы (например, строки вместо чисел). """

print("Введите Цену")
price = input()
print("Скидка")
discount = input()


def discounted(price, discount, max_discount=20):
    try:
        int(price), int(discount)
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except ValueError:
        return "Ошибка, одно из значений не является целым числом"


print(discounted(price, discount))
