import multiprocessing
from datetime import datetime

# 'Задача "Многопроцессное считывание"

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            else:
                all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов 0:00:03.129659 (линейный вызов)
#start = datetime.now()
#for filename in filenames:
#    read_info(filename)
#end = datetime.now()
#time1 = end - start
#print(f'{time1} (линейный вызов)')

# Многопроцессный вызов  0:00:01.892994 (многопроцессный вызов)

if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
        end = datetime.now()
        time2 = end - start
        print(f'{time2} (многопроцессный вызов)')
