# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize('prepare_data', [pytest.param((2, 2, 1), marks=pytest.mark.skip('Ждем доработку для двоек')),
                                          pytest.param((4, 4, 1), marks=pytest.mark.smoke),
                                          pytest.param((1, -1, -1), marks=pytest.mark.negative)],
                         ids= ['positive', 'positive2', 'negative'])
def test_01(prepare_data):
    a, b, result = prepare_data
    assert all_division(a, b) == result
