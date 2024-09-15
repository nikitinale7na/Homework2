from threading import Thread as Tr
from time import sleep
from datetime import datetime


# Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество записываемых слов,
# file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл
# с прерыванием после записи каждого на 0.1 секунду. В конце работы функции вывести строку
# "Завершилась запись в файл <название файла>".

# start_time = time()


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


# После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:
# 10, example1.txt
# 30, example2.txt
# 200, example3.txt
# 100, example4.txt

# start_time = time()
time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
#finish_time = time()

finish_time = datetime.now()
time_res = finish_time - time_start
print(f'Работа потоков {time_res}')

# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
# 10, example5.txt
# 30, example6.txt
# 200, example7.txt
# 100, example8.txt

time_start = datetime.now()
tr_1 = Tr(target=wite_words, args=(10, 'example5.txt'))
tr_2 = Tr(target=wite_words, args=(30, 'example6.txt'))
tr_3 = Tr(target=wite_words, args=(200, 'example7.txt'))
tr_4 = Tr(target=wite_words, args=(100, 'example8.txt'))

tr_1.start()
tr_2.start()
tr_3.start()
tr_4.start()

tr_1.join()
tr_2.join()
tr_3.join()
tr_4.join()

finish_time = datetime.now()
time_res = finish_time - time_start
print(f'Работа потоков {time_res}')
