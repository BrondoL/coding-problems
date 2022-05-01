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
    lr = 0
    rl = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                lr += arr[i][j]
            if i + j == len(arr) - 1:
                rl += arr[i][j]
    return abs(lr - rl)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
