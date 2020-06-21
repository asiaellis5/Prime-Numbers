
def prime_numbers_to_100():
   for val in range(1, 101):
     count = 0
     for i in range(2, val//2 + 1):
       if(val % i == 0):
         print(val)



prime_numbers_to_100()