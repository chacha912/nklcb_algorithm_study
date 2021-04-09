import math

def factorization(n):
    index = 2
    while n != 1:
        if index > math.sqrt(n):
            print(int(n))
            return

        if n % index == 0:
            print(index)
            n /= index
        else:
            index += 1

N = int(input())

factorization(N)
