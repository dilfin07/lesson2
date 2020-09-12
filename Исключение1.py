''''' Перепишите функцию ask_user() из задания про while, чтобы она перехватывала KeyboardInterrupt,
писала пользователю "Пока!" и завершала работу при помощи оператора break '''

while True:
    say = input()


    def ask_user(say):
        try:
            while True:
                dictonary = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", "Пока": "Ну пока"}
                return dictonary.get(say)
        except KeyboardInterrupt:
            return "Пока"
    break

print(ask_user(say))
