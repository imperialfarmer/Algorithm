# -*- using utf-8 -*-
"""
This is to use hash table to solve two-sum problems
The 2sum.txt file contains 1 million integers, both positive and negative (there might 
be some repetitions!).This is your array of integers, with the i^{th}i th row of the 
file specifying the i^{th}i th entry of the array. Your task is to compute the number 
of target values t in the interval [-10000,10000] (inclusive) such that there are 
distinct numbers x,y in the input file that satisfy x+y=t. 

Solution: 427
"""
import sys

def prepareData(fileName,lb,ub):
    file = open(fileName)
    data = []
    for line in file:
        num = int(line)
        data.append(num)
    file.close()

    values = [True] * len(data)

    hash_table = dict(zip(data, values))

    target = []
    for i in range(lb,ub+1):
        target.append(i)

    return hash_table, target


def findTarget(hash_table,target):
    count = 0
    i = 0
    for t in target:
        for key in hash_table.keys():
            paired_key = t - key
            if paired_key != key and paired_key in hash_table.keys():
                count += 1
                # print('\n' + str(key) + '+' + str(paired_key) + '=' + str(t))
                
        sys.stdout.write('\rProcessing ' + str(i) + ' ' + str(count))
        sys.stdout.flush()
        i+=1
    print('\n')

    return count
        

if __name__ == '__main__':
    hash_table, target = prepareData('./2sum.txt',-10000,10000)

    print(len(hash_table))
    print(len(target))

    count = findTarget(hash_table,target)
    print('n')
    print('Solution = ', count/2)

