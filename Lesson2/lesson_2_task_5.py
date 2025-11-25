month = input ("Введите номер месяца: ")
season = int (month)
if (season < 1) or (season > 12):
    print("Нет гакоого месяца в году")
elif (season > 2) and (season < 6):
    print("Весна")
elif (season > 5) and (season < 9):
    print("Лето")
elif (season > 8) and (season < 12):
    print("Осень")
else: print ("Зима")
