import inspect
import sys


def plus(a, b):
    return a + b


def test_01():
    assert plus(2, 2) == 4


def test_02():
    assert plus(100, 9) == 108, "Неверный результат"


def test_03():
    assert plus(-1, 1) == 0


def test_zero():
    assert plus(0, 0) == 0