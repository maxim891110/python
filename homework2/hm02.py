var_count = int(input("Введите количество элементов списка "))
# нужно выполнить преобразование строки к числу, применив функцию int().
# Обратите внимание, что функция input() всегда возвращает строку.
my_list = []  # список
i = 0
el = 0
while i < var_count:  # пока
    my_list.append(input("Введите следующее значение списка "))
    i += 1
    # list.append
# Добавить элемент el в конец списка my_list
for elem in range(int(len(my_list) / 2)):  # диапазон
    # Возвращает длину строки len
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)
