# File: ComparingLinearBinarySearch.py
# Student: Nicole Grimaldos
# UT EID: ng23476
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 11/03/20
# Date Last Modified: 11/03/20
# Description of Program: Compare the performance of linear and binary search
# this is based on a fixed number of n for linear search and binary search
# the program will also print the difference between log2(1000) and the average number
# of probes for binary search.

import random
import math


def linearSearch(lst, key):
    for i in range(len(lst)):
        if key == lst[i]:
            return i
    return -1


def binarySearch(lst, key):
    count = 0
    low = 0
    high = len(lst) - 1
    while high >= low:
        count += 1
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid, count
        else:
            low = mid + 1
    return -low - 1, count


def partOne():
    print("Linear search:")
    lst = list(range(1000))
    random.shuffle(lst)
    n = 10
    while n != 1000000:
        probes = 0
        for x in range(n):
            key = random.choice(lst)
            index = (linearSearch(lst, key) + 1)
            probes += index
        print("  Tests:", format(n, "<9.0f"), end='')
        print("Average probes:", probes / n)
        n = n * 10


partOne()


def partTwo():
    print("Binary search:")
    lst = list(range(1000))
    n = 1000
    probes = 0
    for x in range(n):
        key = random.choice(lst)
        answer = (binarySearch(lst, key))
        count_of_probes = answer[1]
        probes += count_of_probes
    average_probes = probes / n
    print("  Average number of probes:", average_probes)
    log2 = math.log2(1000)
    print("  Differs from log2(1000) by:", log2 - average_probes)


partTwo()
