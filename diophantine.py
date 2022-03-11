# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:02:56 2022

@author: keith
"""

def remove_space(equation):
    equation = ('').join(equation.split())
    return equation

def extract_coefficient(equation):
    a = int(equation.split('x')[0])
    equation = equation.split('x')[1]
    b = int(equation.split('y')[0])
    equation = equation.split('y')[1]
    ans = int(equation.split('=')[1])
    return a,b,ans
equation = ' 2x  -  15y = 24'
 
def swap(a,b):
    temp = a
    a = b 
    b = temp
    return a,b
    
def gcd(a,b):
    a = abs(a)
    b = abs(b)
    if a == 0 or b == 0:
        return 0
    while a != 0:
        if b > a:
            a,b = swap(a,b)
        a = a % b
    return b

def lcm(a,b):
    a = abs(a)
    b = abs(b)
    a_list = [a * i for i in range(1, b + 1)]
    b_list = [b * j for j in range (1, a + 1)]
    i = j = 0
    while True: 
        if a_list[i] < b_list[j]:
            i += 1
        elif b_list[j] < a_list[i]:
            j += 1
        else:
            return a_list[i]
        
def check_solvable(a,b,ans):
    return (ans/gcd(a,b)).is_integer()

def sign(a):
    if (a >= 0):
        return 1
    else:
        return -1
    
        
def find_x0_y0(a,b,ans):
    x0 = 0
    while True:
        y0 = (ans-a*x0)/b
        if y0.is_integer():
            return x0,int(y0)
        else:
            x0 += 1
            
def format_eq_string(a,b,ans):
    eq_string = str(a) + 'x'
    if b > 0:
        eq_string += ' + '
    elif b < 0:
        eq_string += ' - '
    eq_string += str(abs(b)) + 'y = ' + str(ans)
    return eq_string
        
            
def format_ans_string(u,v,x0,y0):
    ans_string = '('
    if x0 != 0:
        ans_string += str(x0)
        if u > 0:
            ans_string += ' + '
        elif u < 0:
            ans_string += ' - '
    if abs(u) > 1: 
        ans_string += str(abs(u))
    elif u == -1 and x0 == 0:
        ans_string += '-'
    ans_string += 'n, '
    if y0 != 0:
        ans_string += str(y0)
        if v > 0:
            ans_string += ' + '
        elif v < 0:
            ans_string += ' - '
    if abs(v) > 1: 
        ans_string += str(abs(v))
    elif v == -1 and y0 == 0:
        ans_string += '-'
    ans_string += 'n)'
    return ans_string

def diophantine(equation):
    a,b,ans = extract_coefficient(remove_space(equation))
    if check_solvable(a,b,ans):  
        u = lcm(a,b) // abs(a)
        v = -sign(a) * lcm(a,b) // b
        x0,y0 = find_x0_y0(a,b,ans)
        print(format_eq_string(a,b,ans),'has as solutions all pairs of the form')
        print('   ',format_ans_string(u,v,x0,y0),'with n an arbitrary integer.')
    else:
        print(format_eq_string(a,b,ans),'has no solution.')