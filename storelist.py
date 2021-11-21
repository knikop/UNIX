from math import e
import random

def Rand (start, end, num):
    res = []
    for n in range(num):
        res.append(random.randint(start, end))
    return res

num = 10
start = 1
end = 90
print(Rand(start, end, num))