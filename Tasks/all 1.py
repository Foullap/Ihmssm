def print_number_k(k, n):
    for _ in range(n):
        print(k)

k = int(input("Введите целое число K: "))
n = int(input("Введите целое число N (N > 0): "))
if n > 0 and k > 0:
    print_number_k(k, n)
else:
    print("Числа N и K должны быть больше 0")
