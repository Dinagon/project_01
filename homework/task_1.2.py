#Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

import random
import time

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
random_songs = random.sample(my_favorite_songs,3) # выбираем 3 случайные песни
total_time = sum([song[1]for song in random_songs])
sum_sound_time= total_time*60   # общее время звучания песен
time_format = time.strftime("%H:%M:%S", time.gmtime(sum_sound_time))  # переводим в формат времени
print(random_songs) # выводим 3 случайные песни
print(f'Три песни звучат ',time_format,)  #  выводим в формате времени
print(f'Три песни звучат ',int(total_time),'минут')  # выводим общее количество минут 3 песен


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

random_songs = random.sample(list(my_favorite_songs_dict.values()), 3) # узнаём время 3 случайных песен
total_sum=int(sum(random_songs)) 
sum_sound_time= total_sum*60
time_format = time.strftime("%H:%M:%S", time.gmtime(sum_sound_time))
print(random_songs)
print('Три песни звучат',total_sum,'минут.') # выводим общее время 3 песен
print(time_format) # выводим общее время в формате времени