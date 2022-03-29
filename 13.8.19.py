tickets = int(input("Введите количество билетов:"))
ticket_price = 0

for i in range(tickets):
    age = int(input("Введите возраст посетителя:"))
    i += 1
    if age < 18:
        print("Проход бесплатный.")
    elif 18 <= age < 25:
        ticket_price += 990
        print("990 руб.")
    elif 25<= age:
        ticket_price += 1390
        print("1390 руб.")
if tickets > 3:
    ticket_price = ticket_price*0.9
    print("Применена скидка 10%, сумма к оплате: ", ticket_price)
else:
    print("Сумма к оплате: ", ticket_price)