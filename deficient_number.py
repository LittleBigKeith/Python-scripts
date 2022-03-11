# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 08:16:01 2022

@author: keith
"""
import sys

def find_divisor(x):
    divisor_list = []
    for i in range(1,x):
        if x % i == 0:
            divisor_list.append(i)
    return divisor_list

def flag(x1,x2):
    if x1 <= x2:
        return 1
    else:
        return -1

try:
    num = input("Enter two strictly positive numbers: ")
    num_list = num.split(' ')
    if len(num_list) != 2:
        raise ValueError
    num1 = int(num_list[0])
    num2 = int(num_list[1])
    if num1 <= 0 or num2 <= 0:
        raise ValueError
except ValueError:
    print("Incorrect input, giving up.")
    sys.exit()

deficient_list = []
length = 0
max_length = 0
max_end = 0
for i in range(num1, num2 + flag(num1, num2), flag(num1,num2)):
    divisor_list = find_divisor(i)
    divisor_sum = sum(divisor_list)
    if divisor_sum < i:
        deficient_list.append(i)
        length += 1
    else:
        if length > max_length:
            max_length = length
            max_end = i-1*flag(num1,num2)
        length = 0
    
if max_length == 0 and not len(deficient_list) == 0:
    max_end = deficient_list[-1]
    max_length = len(deficient_list)

start = max_end - (max_length - 1) * flag(num1, num2)
print(deficient_list)
    
if len(deficient_list) == 0:
    print(f'There is no deficient number between {num1} and {num2}.')
else:
    print(f'The longest sequence of deficient numbers between {num1} and {num2} ranges between {start} and {max_end}.')


