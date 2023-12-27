A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B (B должно быть меньше A): "))

if A <= B:
    print("Ошибка: A должно быть больше B")
else:
    num_segments = 0
    while A >= B:
        A -= B
        num_segments += 1

    remaining_length = A

    print(f"Длина незанятой части отрезка A: {remaining_length}")
