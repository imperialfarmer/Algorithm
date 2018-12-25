# -*- using: utf-8 -*-
"""
The quick sort performance depends on the choice of the pivot points,
Here three choosing ways are tested
1.
2.
3.
"""

import numpy as np

def partition(array, l, r):
    # pivot = l
    p = array[l]
    # i is the position where the number starts to > pivot
    i = j = l + 1
    while j < r:
        if array[j] < p:
            # swap array[j] and array[i]
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp
            i += 1
        j += 1
    return array, i

def quickSort1():
    data = np.fromfile('./quickSort.txt',dtype=int,sep='\n')
    print(data)
    print(len(data))


def main():
    test_array = [3,8,2,5,1,4,7,6]
    print('-- Before partition --')
    print(test_array)
    partitioned_array = partition(test_array,0,len(test_array)-1)
    print('-- After partition --')
    print(partitioned_array)

    print('\n-- Method 1 --')
    quickSort1()

if __name__ == '__main__':
    main()
    
