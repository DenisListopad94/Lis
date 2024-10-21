from time import sleep
from functools import lru_cache


@lru_cache
def recursive(n):
    if n == 1:
        return 1
    else:
        print('wait')
        sleep(0.4)
        return n + recursive(1)


print(recursive(int(1)))
print(recursive(int(1)))
print(recursive(int(310)))
print(recursive(int(310)))
print(recursive(int(31)))
