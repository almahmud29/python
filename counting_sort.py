#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    # n = len(arr)
    m = max(arr)
    # print(n)
    # print(m)
    result = [0]*(m+1)
    
    # print("length of result is: ", len(result))
    # print(len(result))
    # r = range(result)
    for i in range(len(arr)):
        # result[arr[i-1]]+=1
        # print(arr[i])
        result[arr[i]]+=1
        # print(result[arr[i]])
        # print(len(result))
        # print(result)

    return result

# Driver Code 
arr = [1, 0, 2, 2, 1, 1, 2, 1]
# diagonal = diagonalDifference(arr)
r = countingSort(arr)
print(r)