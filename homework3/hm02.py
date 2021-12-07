# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

name = input('name ')
surname = input('surname ')
year = int(input('year '))
city = input('city ')
email = input('mail ')
telephone = input('telephone ')


def my_func(name, surname, year, city, mail, telephone):
    return ' '.join([name, surname, year, city, mail, telephone])


print(my_func(surname='Гурьянов', name='Максим', year='1989', city='Казань', mail='@mail.ru', telephone='+79503'))
