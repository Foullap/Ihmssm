def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    number = int(input("Введите число: "))
    if is_prime(number):
        print(f"{number} - простое число")
    else:
        print(f"{number} - не является простым числом")

