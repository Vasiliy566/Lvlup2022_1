import math

n = 100000000
for i in range(2, int(math.sqrt(n)), 1):
    if n % i == 0:
        print(i)
        print(n / i)
