test_str = input("введите строку ")
test_word = []
num = 1
for el in range(test_str.count(' ') + 1):  # диапазон
    test_word = test_str.split()  # разделитель
    if len(str(test_word)) <= 10:  # Возвращает длину строки
        print(f" {num} {test_word[el]}")
        num += 1
    else:
        print(f" {num} {test_word[el][0:10]}")
        num += 1
