def number_to_words(num):
    numbers = {
        1: 'один',
        2: 'два',
        3: 'три',
        4: 'четыре',
        5: 'пять',
        6: 'шесть',
        7: 'семь',
        8: 'восемь',
        9: 'девять',
        10: 'десять',
        11: 'одиннадцать',
        12: 'двенадцать'
    }

    if num in numbers:
        return numbers[num]
    else:
        return ""

if __name__ == "__main__":
    for i in range(1, 13):
        word = number_to_words(i)
        if word:
            print(f"{i} - {word}")
