from time import time
import math

def prime_numbers_to_100():
   for val in range(1, 101):
     count = 0
     for i in range(2, val//2):
       if(val % i == 0):
         count += 1
         break
     if(count == 0 and val != 1):
       print(val)


t0 = time()
prime_numbers_to_100()
t1= time()

print("Time taken:", t1 - t0)

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

