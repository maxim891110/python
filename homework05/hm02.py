#  Создать текстовый файл (не программно), сохранить в нем несколько строк,
#  выполнить подсчет количества строк, количества слов в каждой строке.

my_file = open("file.txt", "r")
with my_file as file:
    my_list = file.readlines()
for i in range(len(my_list)):
    new_list = my_list[i].split()
    print(f'Количество строк {len(my_list)}. В {i + 1}-ой строке {len(new_list)} слов(а)')