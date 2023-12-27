def calculate_hypotenuse(cathetus1, cathetus2):
    hypotenuse = (cathetus1**2 + cathetus2**2)**0.5
    return hypotenuse

def main():
    cathetus1 = float(input("Введите длину первого катета: "))
    cathetus2 = float(input("Введите длину второго катета: "))
    hypotenuse = calculate_hypotenuse(cathetus1, cathetus2)
    print("Длина гипотенузы: ", hypotenuse)

if __name__ == "__main__":
    main()