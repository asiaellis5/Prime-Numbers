from time import time
import math

def prime_numbers():
  for val in range(2, 101):
    prime = True
    for i in range(2, int(math.sqrt(val))+1):
      if(val % i == 0):
        prime = False
    if prime:
        print(val)


t0 = time()
prime_numbers()
t1= time()

print("Time taken:", t1 - t0)

def eratosthenes(n):
  sieve = [True] * (n + 1)
  for p in range(2, n + 1):
      if (sieve[p]):
        print(p)
        for i in range(p, n + 1, p):
          sieve[i] = False


t0 = time()
eratosthenes(100)
t1= time()

print("Time taken:", t1 - t0)