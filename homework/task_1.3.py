number_of_month = int(input('Введите номер месяца:'))  # принимаем от пользователя номер месяца

if number_of_month == 1:                   # возвращаем название месяца и количество дней в нём
    print('Вы ввели Январь. 31 день')
elif  number_of_month == 2:
    print('Вы ввели Февраль. 28 дней')   
elif  number_of_month == 3:
    print('Вы ввели Март. 31 день')   
elif  number_of_month == 4:
    print('Вы ввели Апрель. 30 дней') 
elif  number_of_month == 5:
    print('Вы ввели Май. 31 день') 
elif  number_of_month == 6:
    print('Вы ввели Июнь. 30 дней') 
elif  number_of_month == 7:
    print('Вы ввели Июль. 31 день') 
elif  number_of_month == 8:
    print('Вы ввели Август. 31 день') 
elif  number_of_month == 9:
    print('Вы ввели Сентябрь. 30 дней') 
elif  number_of_month == 10:
    print('Вы ввели Октябрь. 31 день') 
elif  number_of_month == 11:
    print('Вы ввели Ноябрь. 30 дней')
elif  number_of_month == 12:
    print('Вы ввели Декабрь. 31 день') 
else:
    print('Такого месяца нет!')