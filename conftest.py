import pytest
import datetime


@pytest.fixture(scope='class')
def time_class(request):
    print(f'Время начала выполнения тестов в классе {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}') #как работать с таймером украл отсюда https://docs-python.ru/standart-library/modul-time-python/funktsija-time-modulja-time/
    yield
    print(f'Время окончания выполнения тестов в классе {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


@pytest.fixture()
def time_test():
    begin = datetime.datetime.now()
    yield
    end = datetime.datetime.now()
    print(f'Время выполнения теста {end - begin}')