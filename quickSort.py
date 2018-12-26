# -*- using: utf-8 -*-
"""
The quick sort performance depends on the choice of the pivot points,
Here three choosing ways are tested
1. always using the first element of the array as the pivot element
2. always using the final element of the given array as the pivot element
3. using 'median'
"""

import numpy as np
import math


def swap(array,i,j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
    return array

def partition(array, l, r):
    # pivot = l
    p = array[l]
    # i is the position where the number starts to > pivot
    i = j = l + 1
    while j <= r:
        if array[j] < p:
            # swap array[j] and array[i]
            swap(array,i,j)
            i += 1
        j += 1
    # swap the first one (pivot) with the last one in lesser partition
    array = swap(array,0,i-1)
    return array, i-1 # i-1 is how many elements are swaped


def pivot(array, mode):
    # mid = math.floor(len(array))
    # avg = np.average(array,axis=0)
    # avgPos = 0
    # for i in range(len(array)):
    #     if array[i] == avg:
    #         avgPos = i
    n = len(array)
    pos = -1
    if mode == 0:
        # always using the first element of the array as the pivot element
        pos = 0
    elif mode == 1:
        # always using the final element of the given array as the pivot element
        pos = n-1
    elif mode == 2:
        # using 'median'
        first = array[0]
        final = array[-1]
        if n%2 == 0:
            k = int(n/2) - 1
        else :
            k = int((n-1)/2)
        mid = array[k]

        if (first - mid)*(final - mid) < 0:
            # mid is the 'median'
            pos = k
        elif (mid - first)*(final - first) < 0:
            # first is the 'median'
            pos = 0
        else:
            # final is the 'median'
            pos = n-1
        
    assert pos != -1, 'WRONG MODE'
    return pos
    

def quickSort(array, mode = 0):
    n = len(array)

    if n <= 1:
        # base case, return array and no comparison
        return array, 0
    else:
        pivotPos = pivot(array,mode)

        # swap the pivot point with the first one
        array = swap(array,0,pivotPos)

        # do partition
        array,splitPos = partition(array,0,len(array)-1)
        array[:splitPos], leftCount = quickSort(array[:splitPos],mode)
        array[splitPos+1:], rightCount = quickSort(array[splitPos+1:],mode)

        return array, leftCount+rightCount+(n-1)


def main():
    test_array = [3,8,2,5,1,4,7,6]
    print('-- Before partition --')
    print(test_array)
    partitioned_array = partition(test_array,0,len(test_array)-1)
    print('-- After partition --')
    print(partitioned_array)

    print('\n-- Method 1 --')
    array = np.fromfile('./quickSort.txt',dtype=int,sep='\n')
    array,count1 = quickSort(array,0)
    print(array)
    print(count1)

    print('\n-- Method 2 --')
    array = np.fromfile('./quickSort.txt',dtype=int,sep='\n')
    array,count2 = quickSort(array,1)
    print(array)
    print(count2)

    print('\n-- Method 3 --')
    array = np.fromfile('./quickSort.txt',dtype=int,sep='\n')
    array,count3 = quickSort(array,2)
    print(array)
    print(count3)

if __name__ == '__main__':
    main()
    
