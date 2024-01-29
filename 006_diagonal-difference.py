# link: https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem

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
    l = len(arr)
    sum_left = 0
    sum_right = 0
    
    for i in range(l):
        sum_left += arr[i][i]
        sum_right += arr[i][(l - 1) - i]
    
    return abs(sum_left - sum_right)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
