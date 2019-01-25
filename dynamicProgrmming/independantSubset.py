# -*- using: utf-8 -*-
"""
Find the maximum-weight independant subset (IS)
Choice of 1, 2, 3, 4, 17, 117, 517, 997:
10100110
"""

def ReadPath(fileName):
    file = open(fileName)
    index = 0
    num = 0
    w = {}
    for line in file:
        if index == 0:
            num = int(line)
        else:
            w[index] = int(line)
        index += 1
    file.close()

    return w


def FindWIS(w):
    a = [0]*(len(w)+1)
    a[1] = w[1]
    n = len(a)-1
    for i in range(2,n+1):   
        a[i] = max(a[i-1],a[i-2]+w[i])
        i += 1
    # print('\n')
    # print(a)
    b = [0]*(n+1)
    j = n
    while j >= 1:
        # print(str(a[j-1])+' | '+str(a[j-2])+'+'+str(path[i-1]))
        if a[j-1] >= a[j-2]+w[j]:
            # print('case 1')
            j-=1
        else:
            # print('case 2')
            b[j] = 1
            j-=2
        # print('\n->',j)
        # print(a[j])
        # print(b)
        # input('')

    return a,b


if __name__ == '__main__':
    path = ReadPath('./mwis.txt')
    a,b = FindWIS(path)
    # print(len(b))
    # print(b)
    test = [1, 2, 3, 4, 17, 117, 517, 997]
    solution = [0]*len(test)
    for i in range(len(test)):
        if b[test[i]] == 1:
            solution[i] = 1
    
    print('\nSolution = ',solution)

    
