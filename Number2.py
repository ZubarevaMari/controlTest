# Зубарева Мария Олеговна
# 44-22-122, вариант 12, №2
import math
import unittest


def func(args):
    res = []
    if len(args) == 0:
        print("Ошибка. Строка пустая")
        return None
    for x in args:
        if type(x) != int and type(x) != float:
            print("Ошибка. Необходимо ввести число")
            return None
        if x < 1:
            a = x**2
            y = math.sin(x + x ** 2)
        elif x >= 1:
            y = x * (x + 0.3) ** (1 / 2)
        res.append(y)
    return res


class TestSolver(unittest.TestCase):
    def test_size(self):
        self.assertIsNone(func([]), 'Тест 1')

    def test_list1(self):
        self.assertListEqual(func([2, 0, -3]), [3.03315017762062, 0, -0.27941549819892587281155544661189])

    def test_list2(self):
        self.assertIsNone(func(["34", "jhh"]), 'Тест 3')


if __name__ == "__main__":
    unittest.main()


