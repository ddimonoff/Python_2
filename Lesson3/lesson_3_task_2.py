from smartphone import Smartphone

my_smartphone = [
    Smartphone('Realme', 'GT7 Pro', '+79360483647'),
    Smartphone('Samsung', 'Galaxy S25 Ultra', '+791793747836'),
    Smartphone('Xiaomi', 'Mi 14T Pro', '+79575384631'),
    Smartphone('Honor', 'Magic 7 Pro', '+79286437829'),
    Smartphone('HUAWEI', 'Pura 70 Ultra', '+79627463759')
]
for smartphone in my_smartphone:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model} - {smartphone.phone_number}")
print("Конец списка")
