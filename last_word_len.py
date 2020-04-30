"""
last_word_len -> s String
return last word len

For a given string(s) of letters and spaces return the lenght  of the last word.

A 'word' is a sequence of letters

Ex. 'This is a test' - > reuturns 4 since test has 4 letters

"""
def last_word_len(s):
  words = []
  words.append(s.split())
  last_word_length = 0
  w1 = ''

  for word in words[0]:
      if len(word)>1:
          last_word_length = len(word)
          w1 = word
  return w1, last_word_length 


def test_cases():
    print('Test 1: ','Bob like a','| Result:',last_word_len('Bob like a'))
    print('Test 2: ','Bob like a pig','| Result:',last_word_len('Bob like a pig'))
    print('Test 3: ','','| Result:',last_word_len(''))

def main():
    print('---Test Cases--- Print lenght of last word on a given string with letters and spaces Note: a word is a sequence of letters \n')
    test_cases()
    
if __name__ == "__main__":
    main()