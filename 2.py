# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных
# о пользователе одной строкой.

name = input('Введите своё имя -')
surname = input('Введите сво фамилию -')
years = int(input('Введите свой возраст -'))
city = input('Введите свой город - ')
email = input('Введите свой email - ')
phone = input('Введите сво телефон')
def my_func(name, surname, years, city, email, phone):
     return ' '.join([name, surname, years, city, email, phone])
print(my_func(name = 'Aleksandr', surname = 'kolesnikov', years = '23', city = 'Novovoronezh', email = 'name_email@mail.ru', phone = '8-980-344-91-32'))