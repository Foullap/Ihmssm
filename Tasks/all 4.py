A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B (B должно быть больше A): "))

if A >= B:
    print("Число B должно быть больше числа A")
else:
    sum_all = 0
    sum_even = 0
    sum_odd = 0

    for num in range(A, B+1):
        sum_all += num
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    print(f"Сумма всех чисел от {A} до {B}: {sum_all}")
    print(f"Сумма четных чисел от {A} до {B}: {sum_even}")
    print(f"Сумма нечетных чисел от {A} до {B}: {sum_odd}")
