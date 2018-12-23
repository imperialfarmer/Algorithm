# -*- using: utf-8 -*-
"""
This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, 
with no integer repeated.

Your task is to compute the number of inversions in the file given, where the i^{th}i th row of 
the file indicates the i^{th}i thentry of an array.

Because of the large size of this array, you should implement the fast divide-and-conquer 
algorithm covered in the video lectures.

The numeric answer for the given input file should be typed in the space below.

So if your answer is 1198233847, then just type 1198233847 in the space provided without any 
space / commas / any other punctuation marks. You can make up to 5 attempts, and we'll use the 
best one for grading.

(We do not require you to submit your code, so feel free to use any programming language you want 
--- just type the final numeric answer in the following space.)

[TIP: before submitting, first test the correctness of your program on some small test files or 
your own devising. Then post your best test cases to the discussion forums to help your fellow students!]

* Solution: 2407905288
"""
import numpy as np
import math


def readData(fileName):
    file = open(fileName)
    data = np.fromfile(file, dtype=int,sep='\n')
    print(len(data))
    print(data)

    return data


def splitCount(array1, array2):
    # array1 and array2 have been sorted already
    i = j = count = 0
    array3 = []
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            array3.append(array1[i])
            i += 1
        elif array1[i] > array2[j]:
            count += len(array1[i:])
            array3.append(array2[j])
            j += 1
    # fill arrays with the missed part of array1 and array2
    array3.extend(array1[i:])
    array3.extend(array2[j:])
    return array3, count


def inversionCount(array):
    n = len(array)
    if n <= 1:
        return array, 0
    else:
        mid = int(n/2)
        left = array[:mid]
        right = array[mid:]

        array1,c1 = inversionCount(left)
        array2,c2 = inversionCount(right)
        array3,c3 = splitCount(array1, array2)
        return array3, (c1+c2+c3)

def brute(array):
    count = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                count += 1
        if (i+1)%1000 == 0:
            print(str(i+1) + '/' + str(len(array)) + '\r')
    return count


def main(fileName):
    array = readData(fileName)
    sortedArray, count = inversionCount(array)
    print('dac   = ', count)
    print('brute =  2407905288')


if __name__ == '__main__':
    main('inversion_data.txt')
