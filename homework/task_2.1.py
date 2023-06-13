
# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def maximum(arr): # функция возврата наибольшего числа в списке
    max = arr[0]
    for i in arr:
        if i > max:
          max = i
    return max

def minimum(arr):  # функция возврата наименьшего числа в списке
    min = arr[0]
    for i in arr:
        if i < min:
          min = i
    return min

list1=[4,6,2,1,9,63,-134,566]   # 1 список
result1 = maximum(list1)
result2 = minimum(list1)
print('max =',result1,'min =',result2) # вывод наибольшего и наименьшего числа  1 списка

list2=[-52, 56, 30, 29, -54, 0, -110]  # 2 список
result1 = maximum(list2)
result2 = minimum(list2)
print('max =',result1,'min =',result2)  # вывод наибольшего и наименьшего числа 2 списка

list3=[42, 54, 65, 87, 0]    # 3 список
result1 = maximum(list3)
result2 = minimum(list3)
print('max =',result1,'min =',result2)  # вывод наибольшего и наименьшего числа  3 списка

list4=[5]                    # 4 список
result1 = maximum(list4)
result2 = minimum(list4)
print('max =',result1,'min =',result2)   # вывод наибольшего и наименьшего числа  4 списка