# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.smoke
def test_01():
    assert all_division(2, 2) == 1
@pytest.mark.acceptance
def test_02():
    assert round(all_division(975132, 123452), 2) == 7.9
@pytest.mark.negative
@pytest.mark.acceptance
def test_03_ngt():
    assert all_division(-8, -4) == 2
@pytest.mark.acceptance
@pytest.mark.negative
def test_04_ngt():
    assert all_division(19) == 19
@pytest.mark.acceptance
@pytest.mark.negative
def test_05_ngt():
    with pytest.raises(ZeroDivisionError):
        all_division(0, 0)
