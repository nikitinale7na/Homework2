import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        hum1 = runner.Runner('Иванов')
        for i in range(10):                 # метод, в котором создаётся объект класса Runner с произвольным именем.
            hum1.walk()                               # Далее вызовите метод walk у этого объекта 10 раз.

        self.assertEqual(hum1.distance, 50)    # После чего методом assertEqual сравните distance этого объекта
                                                       # со значением 50.

    def test_run(self):
        hum1 = runner.Runner('Иванов')
        for i in range(10):
            hum1.run()                                 # то же, что и для метода test_walk

        self.assertEqual(hum1.distance, 100)

    def test_challenge(self):
        hum1 = runner.Runner('Иванов')
        hum2 = runner.Runner('Петров')
        for i in range(10):
            hum1.walk()
            hum2.run()               # тестируем на 2 разных бегунах разные методы с разными дистанциями

        self.assertNotEqual(hum1.distance, 150)


if __name__ == '__main__':
    unittest.main()
