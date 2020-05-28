import requests
import pytest

import allure

data_1 = [1,2]
data_2 = [4,5]


@pytest.mark.parametrize('a', data_1)
@pytest.mark.parametrize('b', data_2)
def test_parametrize_1(a, b):
    print('\n测试数据为\n{}，{}'.format(a, b))


