# price=input()
# price = abs(float(price))
# print(type(price))


price = input()
discount = input()


def is_int(price):
    try:
        int(price), int(discount)
        return True
    except ValueError:
        return "Не является целым числом"


print(is_int(price))
