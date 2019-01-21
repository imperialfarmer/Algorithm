# -*- using: utf-8 -*-
"""
The code for heap class
Solution: 46831213
"""

import sys

def readData(fileName):
    file = open(fileName)
    array = []
    for line in file:
        array.append(int(line))
    file.close()

    return array


class binHeap:
    def __init__(self, mode):
        self.heapList = []
        self.size = 0
        self.mode = mode
        if mode != 'max' and mode != 'min':
            print('   ! Heap is set as default: min heap')

    def bottomToTop(self,i):
        while i != 0:
            # if the leaf is larger than the root, swap them until the very begining (for min heap) 
            # and vice versa
            lesserOne = self.heapList[i] if self.mode == 'max' else self.heapList[(i-1) // 2]
            largerOne = self.heapList[i] if self.mode == 'min' else self.heapList[(i-1) // 2]
            if lesserOne > largerOne:
                tmp = self.heapList[(i-1) // 2]
                self.heapList[(i-1) // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = (i-1) // 2

    def insert(self,a):
        self.heapList.append(a) # add new number into list to the last position
        self.bottomToTop(self.size)
        self.size += 1

    def build(self, array):
        for num in array:
            self.insert(num)

    def extract(self):
        val = self.heapList[0]
        if self.size == 1:
            self.heapList = []
        elif self.size > 1:
            self.heapList[0] = self.heapList[-1]
            i = 0
            next = 0
            while 2*i+1 < self.size:
                if 2*i+2 >= self.size-1:
                    next = 2*i+1
                else:
                    left = self.heapList[2*i+1]
                    right = self.heapList[2*i+2]

                    if left < right:
                        next = 2*i+1 if self.mode == 'min' else 2*i+2
                    else:
                        next = 2*i+1 if self.mode == 'max' else 2*i+2

                # print('choose ', next)
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[next]
                self.heapList[next] = tmp
                i = next

            self.heapList.pop(-1)
        
        self.size -= 1

        return val


def findMedian(array):
    """
    median is defined as
    even: k/2
    odd: (k+1)/2
    so the high heap has size h and low heap has size l
    then 0 =< l - h <= 1, extract the max of low heap to be the median
    """
    lowHeap = binHeap('max')
    highHeap = binHeap('min')

    medians = []

    lowHeap.insert(array[0])
    medians.append(array[0])

    for num in array[1:]:
        # print('\n')
        # print('inserting ', num)
        lb = lowHeap.extract()
        # print('lb = ', lb)

        lowHeap.insert(lb)

        if num > lb:
            highHeap.insert(num)
        else:
            lowHeap.insert(num)

        lsize = lowHeap.size
        hsize = highHeap.size

        # print(str(lsize) + '|' + str(hsize))

        if lsize - hsize > 1:
            val = lowHeap.extract()
            highHeap.insert(val)
            # print('adjust low -1')
        elif lsize - hsize < 0:
            val = highHeap.extract()
            lowHeap.insert(val)
            # print('adjust high - 1')

        median =lowHeap.extract()
        medians.append(median)
        lowHeap.insert(median)
        # print(median)

    # print(lowHeap.heapList)
    # print(highHeap.heapList)
    # print('\n')
    
    return medians


if __name__ == '__main__':
    testArray = [5,6,2,3,41,6,4,123]
    heap1 = binHeap('min')
    heap1.build(testArray)
    # print(heap1.heapList)

    medians1 = findMedian(testArray)
    # print(medians1)

    array = readData('./Median.txt')
    medians2 = findMedian(array)
    # print(medians2)
    print(sum(medians2))







    