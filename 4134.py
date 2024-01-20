import math

def next_prime(n):
    while True:
        cnt = 1
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                cnt += 1
            if cnt >= 2:
                break
        if cnt == 1:
            return n
        n += 1


T = int(input())

for _ in range(T):
    n = int(input())
    if n == 0 or n == 1:
        print(2)
    else:
        print(next_prime(n))