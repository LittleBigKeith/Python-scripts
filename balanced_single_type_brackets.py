# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:23:30 2022

@author: keith
"""

return_dict = {0:1, 1:-1}

bracket = ['(',')','[',']','{','}']

def balanced_brackets_in(pattern):
    bracket_ind = 0
    single_type = -1
    for i in pattern:
        if i != ' ':
            if i not in bracket:
                return None
    for i in pattern:
        if i != ' ':        
            bracket_ind += return_dict[list.index(bracket,i) % 2]
            if single_type == -1:
                single_type = list.index(bracket,i) // 2
            elif list.index(bracket,i) // 2 != single_type:
                return None
            if bracket_ind < 0:
                return False
    if bracket_ind != 0:
        return False
    return True

