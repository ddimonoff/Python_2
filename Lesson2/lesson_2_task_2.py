is_year_leap = input ("Введите год: ")
year = int (is_year_leap)
if (year % 4 > 0):
    print (is_year_leap+ " год не високосный")
else:
    print (is_year_leap + " год високосный")