while True:
    try:
        x = int(input("Запустите меня в ГитХаб! Я программа номер 10. Напишите пожалуйста номер:\n "))
        break
    except ValueError:
        print ("Вы ошиблись. Попробуйте еще раз…")