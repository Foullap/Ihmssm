N = int(input("Введите целое число N: "))

is_power_of_3 = False
while N != 1:
    if N % 3 != 0:
        break
    N = N / 3

if N == 1:
    is_power_of_3 = True

print(is_power_of_3)