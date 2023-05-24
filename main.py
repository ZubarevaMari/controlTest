# Зубарева Мария Олеговна
# 44-22-122, вариант 12, №1
import math
import argparse


def func(args):
    res = []
    for x in args:
        if x < 1:
            y = math.sin(x + x ** 2)
        elif x >= 1:
            y = x * (x + 0.3) ** (1 / 2)
        res.append(y)
    return res


def getArgs():
    parser = argparse.ArgumentParser(description='Change numbers')
    parser.add_argument('numbers', metavar='N', type=float, nargs='+',
                        help='A numbers for converting')

    return parser.parse_args().numbers


nums = getArgs()
print(func(nums))
# Исключения атоматические)

