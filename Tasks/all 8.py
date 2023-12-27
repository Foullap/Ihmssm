def taxi_fare(distance):
    base_fare = 240
    additional_fare = (distance // 0.14) * 15
    total_fare = base_fare + additional_fare
    return total_fare

distance = float(input("Введите расстояние поездки в километрах: "))
total_payment = taxi_fare(distance)
print("Итоговая сумма оплаты такси:", total_payment)
