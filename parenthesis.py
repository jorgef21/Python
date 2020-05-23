"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:

Input: "()"
Output: true
Example 3:

Input: "(]"
Output: false
"""
def isValid(s):
        parens = ['()', '[]', '{}'] 
        while True:
            orig_len = len(s)
            for p in parens: 
                s = s.replace(p, '')
                if len(s) == 0: 
                    return True
                if orig_len == len(s):
                    return False

def main():
    print(isValid('()'))
    print(isValid('(}'))
    print(isValid('[}'))
    print(isValid('({})'))
    print(isValid(''))

if __name__=='__main__':
    main()