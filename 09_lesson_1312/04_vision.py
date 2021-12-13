# переменные бывают локальными и глобальными
from zmq.backend import first


def m():
    firstVar = 10
    secondVar = 20
    return firstVar * secondVar

print(m())
print(firstVar)
