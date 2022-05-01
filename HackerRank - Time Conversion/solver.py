#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    time = s.split(":")
    h = time[0]
    if "PM" in s:
        if h != "12":
            time[0] = str(int(h) + 12)
    else:
        if h == "12":
            time[0] = "00"
    s = ":".join(time)
    return s[:-2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
