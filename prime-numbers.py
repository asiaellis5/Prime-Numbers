from time import time

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



