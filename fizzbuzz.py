"""
Fizzbuzz problem using modular code
"""
def divisible_by(num,denominator):
    if num % denominator == 0:
        return True
    else:
        return False

def divisible_three(num):
 if divisible_by(num,3):
    return True   
 else:
    return False

def divisible_five(num):
    if divisible_by(num,5):
        return True
    else:
        return False 

def divisible_fifteen(num):
    if divisible_by(num,15):
        return True
    else:
        return False

def fizz_buzz(min,max):
    f = 'Fizz'
    b = 'Buzz'

    for num in range(min,max+1):
        if divisible_fifteen(num):
            print(f+b)
        elif divisible_three(num):
            print(f)
        elif divisible_five(num):
            print(b)
        else:
            print(num)
def test_cases():
    print('-----Number divisible by 3-----')
    if divisible_three(3):
        print('Num:',3,'Test Passed!')
    if not divisible_three(2):
        print('Num: ',2,'Test Failed')
    
    print('\n-----------')
    print('==FizzBuzz range 1,20==')
    fizz_buzz(1,20)

if __name__ == "__main__":
    #Entry point will call the function test_cases to evaluate/test the functions
    test_cases()
