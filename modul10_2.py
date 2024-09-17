from threading import Thread as Th
from time import sleep
# Задача "За честь и отвагу!"
# Создайте класс Knight с соответствующими описанию свойствами.
# Создайте и запустите 2 потока на основе класса Knight.
# Выведите на экран строку об окончании битв.


class Knight(Th):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemies_ = 100
        num_day = 0
        for i in range(enemies_):
            if enemies_ > 0:
                enemies_ -= self.power
                num_day += 1
                sleep(1)
                print(f'{self.name} сражается {num_day} день, осталось {enemies_} воинов')
                if enemies_ <= 0:
                    print(f'{self.name} одержал победу спустя {num_day} дней!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)


first_knight.start()
second_knight.start()


first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')