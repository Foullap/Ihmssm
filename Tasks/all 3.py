def calculate_cost(price_per_kg, weight):
    return price_per_kg * weight

price_per_kg = float(input("Введите цену в рублях за 1 кг конфет: "))

weights = [1.2, 1.4, 1.6, 1.8, 2]
for weight in weights:
    cost = calculate_cost(price_per_kg, weight)
    print(f"Стоимость {weight} кг конфет: {cost}")
