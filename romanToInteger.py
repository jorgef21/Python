"""
Convert roman to integer
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
"""
def romanToInt(s):
    v = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    su = 0
    for  i in range(len(s)-1):
        if v[s[i]] < v[s[i+1]]:
            su -= v[s[i]]
        else:
            su += v[s[i]]
    su += v[s[-1]]
    return su    


def main():
    print(romanToInt('III'))
    print(romanToInt('IV'))
    print(romanToInt('CD'))
    print(romanToInt('XL'))

if __name__=='__main__':
    main()
