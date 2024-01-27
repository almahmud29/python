#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    mp = dict()
    n = len(a)
    for i in range(n):
        if a[i] in mp.keys():
            mp[a[i]] += 1
        else:
            mp[a[i]] = 1
            
    # Traverse through map and print
    # frequencies

    for x in mp:
        if mp[x]==1:
        #   print(x);
            single = x
            
    return single


# Driver Code 
arr = [10, 30, 40, 20, 10, 20, 50, 10] 
n = len(arr) 
lonely = lonelyinteger(arr)
print(lonely)