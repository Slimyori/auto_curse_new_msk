import inspect
import sys


import time

sec = time.time()


struct = time.localtime(sec)


print(time.strftime('%d.%m.%Y %H:%M', struct))