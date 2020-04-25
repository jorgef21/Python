
"""
Primer number from 1,100
"""
def prime_number(min,max):
 for num in range(min,max):
  if num > 1:
   for i in range(2,num):
    if num % i == 0:
      break
   else:
    print(num)

if __name__=='__main__':
 prime_number(1,101)