num = input ("Введите число: ")
numb = int (num) + 1
i = 1
for i in range(1, numb) :
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)
print ("Конец списка")