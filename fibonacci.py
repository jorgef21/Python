"""
Fibonacci series 
"""

def fibonacci(terms):
 n1,n2 = 0,1
 count = 0
 if terms <= 0:
  print('Invalid number')
 elif terms == 1:
  print('Seq up to ',terms)
  print(n1)
 else:
  print('Seq:')
  while count < terms:
   print(n1)
   nth = n1+n2
   n1 = n2
   n2 = nth
   count += 1

if __name__=='__main__':
 fibonacci(7)


