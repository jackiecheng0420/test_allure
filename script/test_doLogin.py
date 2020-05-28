import requests
import pytest

from config.conf import *
# data1 是一个列表，每一个元组就是一组测试用例
finalurl = set_ip()
data1 = [('2.5.106', '0', 'b2f192d7525d4e93de9c321f6b238f80')]


@pytest.mark.parametrize("version,unlock_version,sign",data1)

def test_doLogin(version,unlock_version,sign):
    response = requests.get(url=finalurl,
                                params={'version':version,
                                'unlock_version':unlock_version,
                                'sign':sign})
    globals()["a"] = response.json()['top_id']
    globals()["b"] = response.json()['advertising_version']
    print(type(globals()["a"]))


# def test_one1():
#     b = globals()["a"]
#     print(b)

# def test_doUpdataGenres():
#     rep = requests.get(url='http://124.65.176.126:65000/app/content/doUpdateGenres.do',
#                            params={'to':88119,
#                                    'top_id':globals()["a"],
#                                    'version':0,
#                                    'app_version':'2.5.106',
#                                    'advertising_version':0,
#                                    'sign':'2b79efab618d2c9782f9bb058fde95ef'
#                                    })
#     print(rep.json())

if __name__ == '__main__':
    pytest.main(["-s","test_doLogin.py"])