import threading
from threading import Lock, Thread
from random import randint
from time import sleep

# Задача "Банковские операции"

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        transactions = 100
        x = randint(50, 500)
        for i in range(transactions):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += x
            print(f'Пополнение:{x}. Баланс:{self.balance}\n')
            sleep(0.001)

    def take(self):
        transactions = 100
        y = randint(50, 500)
        for i in range(transactions):
            print(f'Запрос на {y}\n')
            if y <= self.balance:
                self.balance -= y
                print(f'Снятие: {y}. Баланс: {self.balance}\n')
            else:
                print(f'Запрос откланен, недостаточно средств\n')
                self.lock.acquire()
                sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
