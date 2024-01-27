#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    a = len(arr)
    left_d = 0
    right_d = 0
    
    for i in range(a):
        left_d = left_d + arr[i][i]
        right_d = right_d + arr[a-1][i]
        a-=1
        
    diag = abs(left_d - right_d)
    return diag

# Driver Code 
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]] 
diagonal = diagonalDifference(arr)
print(arr)
print(diagonal)
