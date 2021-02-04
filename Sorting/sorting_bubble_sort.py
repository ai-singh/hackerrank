#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    count = 0
    for index1 in range(len(a)):
        for index2 in range(index1 + 1, len(a)):
            if a[index1] > a[index2]:
                a[index1], a[index2] = a[index2], a[index1]
                count +=1
    print("Array is sorted in " + str(count) + " swaps.")
    print("First Element: " + str(arr[0]))
    print("Last Element: " + str(arr[-1]))
    

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
