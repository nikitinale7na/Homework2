# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое",
# если результат 1ой функции будет простым числом и "Составное" в противном случае.

def is_prime(func):
    def wrapper(*args):
        x = func(*args)
        count = 0
        for i in range(1, x + 1):
            if x % i == 0:
                count += 1
        return f'Простое \n{x}' if count == 2 else f'Составное \n{x}'
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

result1 = sum_three(2, 3, 5)
print(result1)