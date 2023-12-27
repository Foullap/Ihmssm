def print_numbers_between(a, b):
    count = 0
    for i in range(a, b+1):
        print(i)
        count += 1
    return count

a = int(input("Введите целое число A: "))
b = int(input("Введите целое число B (B должно быть больше A): "))

if b > a:
    count = print_numbers_between(a, b)
    print("Количество чисел: ", count)
else:
    print("Число B должно быть больше A")
