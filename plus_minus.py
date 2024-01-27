#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zer = 0
    for numbers in arr:
        if numbers > 0:
            pos+=1
        elif numbers < 0:
            neg+=1
        else:
            zer+=1
    r = pos+neg+zer
    r1 = pos/r
    r2 = neg/r
    r3 = zer/r
    print("{:.6f}".format(r1))
    print("{:.6f}".format(r2))
    print("{:.6f}".format(r3))


# Driver Code         
plusMinus([1, 5, -2, 0, -6]) 