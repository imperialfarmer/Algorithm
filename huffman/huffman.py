# -*- using: utf-8 -*-
"""
Generate the Huffman code for the data with given probabilities
data is given like {'key': probability}
'0' for lesser ptobability key, '1' for the bigger one
* Solution
    Max length = 19
    Min length = 9
"""

import sys
import operator


def readData(fileName):
    file = open(fileName)
    i = 0
    num = 0
    sum = 0
    data = {}

    # read the frequencies and use string as key
    for line in file:
        if i == 0:
            num = int(line)
        else:
            feq = int(line)
            data[str(i)] = feq
            sum += feq
        i += 1
    file.close()

    # calculate the probability
    for j in range(num):
        data[str(j+1)] = data[str(j+1)]/sum

    sys.setrecursionlimit(num*10)
    
    return data


def huffman(data):
    # Ensure probabilities should have sum of 1
    assert(sum(data.values()) <= 1.+1e-4 and sum(data.values()) >= 1.-1e-4) 

    # Create a new distribution by merging lowest prob. pair
    a1, a2 = lowest_pair(data)

    # Base case of only two symbols, assign 0 or 1 arbitrarily
    if(len(data) == 2):
        return dict(zip([a1, a2], ['0', '1']))

    # replace a1,a2 with a1+a2
    data_prime = data.copy()
    p1, p2 = data_prime.pop(a1), data_prime.pop(a2)
    data_prime[a1 + a2] = p1 + p2

    # Recurse and construct code on new distribution
    code = huffman(data_prime)
    # replace a1+a2 with a1,a2 in hunffman coding
    ca1a2 = code.pop(a1 + a2)
    code[a1], code[a2] = ca1a2 + '0', ca1a2 + '1'

    return code


def lowest_pair(data):
    # Ensure there are at least 2 symbols in the dist.
    assert(len(data) >= 2) 

    sorted_data = sorted(data.items(), key=operator.itemgetter(1))
    return sorted_data[0][0], sorted_data[1][0]


if __name__ == '__main__':
    data = readData('./huffman.txt')
    # print(data)
    code = huffman(data)
    # find the minimum length and maximum length
    length = []
    for binCode in code.values():
        length.append(len(binCode))
    print(' -> Huffman Code')
    print('    Solution max = ', max(length))
    print('             min = ', min(length))
        
    
    
