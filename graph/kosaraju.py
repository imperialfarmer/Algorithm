# -*- using: utf-8 -*-
"""
kosaraju's two pass algorithm is to compute the Strongly Connected Components (SCC)
"""

import numpy as np
import sys


def DFS(G, i, t ,s, f, leader):
    G[i][0] = True
    leader[i] = s
    print(G[i][1:])
    for headIndex in G[i][1:]:
        if not G[headIndex-1][0]:
            print(str(i+1) + '->' + str(headIndex))
            input()
            DFS(G, headIndex-1, t, s, f, leader)
    t += 1
    f[i] = t
    print('f('+str(i+1)+')='+str(t))


def DFSLoop(G, t=0, s=0):
    f = []
    leader = []
    for i in range(len(G)):
        f.append(-1)
        leader.append(-1)

    for i in range((len(G)-1),-1,-1):
        if not G[i][0]:
            s = i
            DFS(nodeList, i, t, s, f, leader)

    print(f)
    print(leader)



def kosaraju(G):
    #! compute on G_rev
    DFSLoop(G)


def readEdgeList(fileName):
    debug = False
    file = open(fileName)
    # edgeList = [] # tail -> head
    count = 1
    # convert the edge list to vertices list
    # in vertices list, the head vertex from this vertex is recorded
    nodeList = []
    tmp = [False]
    nodeCount = 1
    for line in file:
        # edgeList.append([int(line.split()[0]),int(line.split()[1])])
        if int(line.split()[0]) == nodeCount:
            tmp.append(int(line.split()[1]))
        else:
            nodeList.append(tmp)
            if debug:
                print(tmp)
                input()
                print(nodeList)
            tmp = [False]
            nodeCount += 1
            while nodeCount != int(line.split()[0]):
                nodeCount += 1
                nodeList.append([True])
            tmp.append(int(line.split()[1]))

        sys.stdout.write('\rEdge '+str(count)+' Vertex '+str(nodeCount))
        sys.stdout.flush()
        count += 1
    nodeList.append(tmp)
    
    # edgeList = np.array(edgeList)
    nodeList = np.array(nodeList)
    return nodeList


if __name__ == '__main__':
    #! for testing
    if len(sys.argv) != 1:
        print('\n')
        nodeList = readEdgeList('./SCC_test.txt')
        print('\n')
        print(nodeList)

        kosaraju(nodeList)
        print(nodeList)

    else:
        #! code
        # read the edge list in
        print('\nInput edge list in')
        nodeList = readEdgeList('./SCC.txt')

        # check the reading is right
        print('\n')
        print('\nCheck the node list Edge = 5105043 Vertex = 875714')
        print('read in  ', nodeList[1-1])
        print('checked as [1 2 5 6 7 3 8 4]')
        print('--------')
        print('read in  ', nodeList[4-1])
        print('checked as []')
        print('--------')
        print('read in  ', nodeList[-1])
        print('checked as [542446 13655 542447 13656 542448 542449 542450 542451 542452 13660 9434 542453]')   


