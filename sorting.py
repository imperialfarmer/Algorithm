# -*- using: utf-8 -*-

import sys


def insertion(a):
    size = len(a)
    if size == 0:
        return (False, a)
    if size == 1:
        return (True, a)
    for i in range(size-1):
        j = i
        while a[j] > a[j+1] and j >= 0:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
            j -= 1
    return (True, a)

####################################################################

def merge(a1, a2):
    index1 = 0
    index2 = 0
    a = []
    print('from divide')
    print('a1',a1)
    print('a2',a2)
    while index1 < len(a1) or index2 < len(a2):
        output_left = False
        output_right = False
        print(index1)
        print(index2)
        if index1 >= len(a1) and index2 < len(a2):
            output_right = True
            print('case1')
        if index1 < len(a1) and index2 >= len(a2):
            output_left = True
            print('case2')
        if (index1 < len(a1) and index2 < len(a2)):
            print('case2.5')
            if a1[index1] < a2[index2]:
                output_left = True
                print('case3')
            else:
                output_right = True
                print('case4')
        
        if output_left:
            a.append(a1[index1])
            index1 += 1  
        if output_right: 
            a.append(a2[index2])
            index2 += 1

    return a

def divide(a, m):
    index = 0
    a1 = []
    a2 = []
    for num in a:
        if index <= m:
            a1.append(num)
        else:
            a2.append(num)
        index += 1
    return a1, a2

def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        l = 0
        r = len(a) - 1
        m = int( (l+r)/2 )
        left,right = divide(a,m)
        print('left', left)
        print('right', right)
        left = merge_sort(left)
        right = merge_sort(right)
        merged = merge(left,right)
        print('merge', merged)
        print('===========')
        return merged

####################################################################
# fibonachi function
def Fn(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return Fn(n-1) + Fn(n-2)

def main():
    # a1 = [4,6,5,8,12,11,11,15,14]
    # res = insertion(a1)
    # print(res)

    # a2 = [38,27,43,3,9,82,10]
    # res = merge_sort(a2)
    # print(res)

    print(Fn(10))


if __name__ == '__main__':
    main()
        
        
            
