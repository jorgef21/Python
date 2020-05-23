def isPalindrome(x) -> bool:
        if str(x)[::-1]==str(x):
            return True
        return False

def main():
    print('123 -',isPalindrome(123))
    print('121 -',isPalindrome(121))
    print('-121 -',isPalindrome(-121))

if __name__=='__main__':
    main()