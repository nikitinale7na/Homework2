import unittest
import runner_2 as run_2
from unittest import TestCase


class TournamentTest(TestCase):
    all_results = None

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = run_2.Runner('Усейн', 10)
        self.andrey = run_2.Runner('Андрей', 9)
        self.nik = run_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for i, j in value.items():
                res[i] = str(j)
            print(res)

    def test_1(self):
        first_run = run_2.Tournament(90, self.usain, self.nik)
        result = first_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    def test_2(self):
        second_run = run_2.Tournament(90, self.andrey, self.nik)
        result = second_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    def test_3(self):
        third_run = run_2.Tournament(90, self.andrey, self.usain, self.nik)
        result = third_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result


if __name__ == '__main__':
    unittest.main
