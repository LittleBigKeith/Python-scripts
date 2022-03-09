import sys
import string

def print_left_char(i):
    start = (i + 1) * i // 2 % 26
    size = i + 1
    if start + size < 26:
        print(char[start:start+size], end = '')
    else:
        print(char[start:],end = '')
        size = size - (26 - start)
        while(size > 26):
            print(char[:],end = '')
            size = size - 26
        print(char[:size],end = '')
        
def print_right_char(i):
    start = (26 - (i + 1) * i // 2 - i) % 26
    size = i
    if start + size < 26:
        print(char_reverse[start:start+size],end = '')
    else:
        print(char_reverse[start:], end = '')
        size = size - (26 - start)
        while(size > 26):
            print(char[:], end = '')
            size = size - 26
        print(char_reverse[:size], end = '')

try:
    height = int(input("Enter a strictly positive integer: "));
    if height <= 0:
        raise ValueError
except ValueError:
    sys.exit()
    
char = string.ascii_uppercase
char_reverse = char[::-1]

for i in range(height):
    for j in range(height - i - 1):
        print(' ',end = '')
    print_left_char(i)
    print_right_char(i)
    print()