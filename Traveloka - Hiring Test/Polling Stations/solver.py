#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countPollingStation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_CHARACTER_ARRAY region
#

def countPollingStation(n, m, region):
    # Write your code here
    polling_stations = 0

    def dfs(row, col):
        nonlocal polling_stations
        if row < 0 or row >= n or col < 0 or col >= m or region[row][col] == ".":
            return

        region[row][col] = "."
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)

    for i in range(n):
        for j in range(m):
            if region[i][j] == "x":
                polling_stations += 1
                dfs(i, j)

    return polling_stations

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    m = int(input().strip())
    region_rows = n
    region_columns = m

    region = []

    for _ in range(region_rows):
        region.append(list(input().strip()))

    result = countPollingStation(n, m, region)

    fptr.write(str(result) + '\n')

    fptr.close()
