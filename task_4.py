# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time

@pytest.mark.usefixtures('time_class')
class TestTimer:

	def test_vwesdr(self):
		pass

	@pytest.mark.usefixtures('time_test')
	def test_with_fix(self):
		val = 0
		for i in range (110):
			val += i




