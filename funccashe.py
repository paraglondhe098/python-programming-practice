import time
from functools import lru_cache
@lru_cache(maxsize=3)
def delay(n):
    return time.sleep(n)
print("hi")
delay(5)
print("hii")
delay(5)
print("done")
