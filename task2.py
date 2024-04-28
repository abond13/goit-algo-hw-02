from collections import deque
import re

def is_palindrome(string):
    string = re.sub('\W+','', string).lower()
    dq = deque(string)
    while len(dq) > 1:
        if dq.pop() != dq.popleft():
            return False
    return True

print(is_palindrome("А роза упала на лапу Азора!")) # True
print(is_palindrome("1 23-45 43,. 21")) # True
print(is_palindrome("1234543210")) #False