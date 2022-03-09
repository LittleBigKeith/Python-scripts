# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 11:04:36 2022

@author: keith
"""

coin = [100,50,20,10,5,2,1]
coin_n = []

def money(value):
    return '$'+str(value)

amount = int(input('Input the amount: '))
for value in coin:
    coin_n.append(amount // value)
    amount -= value * (amount // value)
print()
if sum(coin_n) == 0:
    print('No coin is needed.')
elif sum(coin_n) == 1:
    single_coin = coin[list.index(coin_n,1)]
    print(f'One coin of value ${single_coin} is needed.')
else:
    print(f'{sum(coin_n)} coins are needed. The detail is:')
    for i in range(len(coin)):
        if coin_n[i] > 0:
            print(f'{money(coin[i]):>8}: {coin_n[i]}')
        