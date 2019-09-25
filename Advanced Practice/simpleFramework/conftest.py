from simpleFramework.framework.Api import Api
from pytest import fixture


#Обычная фиксута под автосоздание объекта класса Api
@fixture(scope="function")
def api():
    return Api()
