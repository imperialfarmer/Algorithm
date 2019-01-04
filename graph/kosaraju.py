# -*- using: utf-8 -*-
"""
kosaraju's two pass algorithm is to compute the Strongly Connected Components (SCC)
"""

import sys


#! sorting algorithms
def merge(array1, array2):
    # array1 and array2 have been sorted already
    i = j = 0
    array3 = []
    while i < len(array1) and j < len(array2):
        if array1[i][1] < array2[j][1]:
            array3.append(array1[i])
            i += 1
        elif array1[i][1] > array2[j][1]:
            array3.append(array2[j])
            j += 1
    # fill arrays with the missed part of array1 and array2
    array3.extend(array1[i:])
    array3.extend(array2[j:])
    return array3


def mergeSort(array):
    n = len(array)
    if n <= 1:
        return array
    else:
        mid = int(n/2)
        left = array[:mid]
        right = array[mid:]

        array1 = mergeSort(left)
        array2 = mergeSort(right)
        array3 = merge(array1, array2)
        return array3


#! graph algorithms
def readEdgeList(fileName):
    debug = False
    file = open(fileName)
    edgeList = [] # tail -> head
    count = 1
    # convert the edge list to vertices list
    # in vertices list, the head vertex from this vertex is recorded
    nodeList = []
    tmp = [False]
    nodeCount = 1
    maxIndex = 1
    for line in file:
        edgeList.append([int(line.split()[0]),int(line.split()[1])])
        if int(line.split()[1]) > maxIndex:
            maxIndex = int(line.split()[1])
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
                nodeList.append([False])
            tmp.append(int(line.split()[1]))

        sys.stdout.write('\r   Edge '+str(count)+' Vertex '+str(nodeCount))
        sys.stdout.flush()
        count += 1
    nodeList.append(tmp)
    file.close()
    
    print('\n')
    print('   Readjust missed nodes')
    maxNum = len(nodeList)
    print('   Current max = '+str(maxNum)+' max in list = '+str(maxIndex))
    while  maxNum < maxIndex:
        nodeList.append([False])
        maxNum += 1
    print('   Now total node num = ', maxNum)
    
    nodeListRev = []
    for i in range(len(nodeList)):
        nodeListRev.append([False])
    
    count = 1
    for pair in edgeList:
        head = pair[0]
        tail = pair[1]
        nodeListRev[tail-1][0] = False
        nodeListRev[tail-1].append(head)
        sys.stdout.write('\r   Grev Edge '+str(count)+'/'+str(len(edgeList))+' generated')
        sys.stdout.flush()
        count += 1

    return nodeList, nodeListRev, len(nodeList)+len(edgeList)


def DFSLoop(G, queueList):
    #! initialize parameters
    global t
    t = 0
    global s
    s = 0

    f = []
    leader = []
    for i in range(len(G)):
        f.append([i+1,-1])
        leader.append(-1)

    #! loop through the graph using DFS
    index = 1
    for i in queueList:
        if not G[i][0]:
            s = i+1
            f,leader = DFS(G, i, f, leader)
        sys.stdout.write('\r   Finish '+str(index)+'/'+str(len(queueList)))
        sys.stdout.flush()
        index += 1

    return f, leader


def DFS(G, i, f, leader):
    debug = False
    global t
    global s
    if debug:
        print('time = ', t)
    G[i][0] = True
    leader[i] = s
    if debug:
        print(G[i][1:])
    if len(G[i]) > 1:
        for headIndex in G[i][1:]:
            if not G[headIndex-1][0]:
                if debug:
                    print(str(i+1) + '->' + str(headIndex))
                    input()
                f,leader = DFS(G, headIndex-1, f, leader)
    t += 1
    f[i][1] = t
    if debug:
        print('f('+str(i+1)+')='+str(t))
        print('leader('+str(i+1)+')='+str(leader[i]))

    return f,leader


def kosaraju(graphDir):
    print('-- Kosaraju\'s Two Pass Algorithm --')
    debug = False
    #! read input
    print('-> Reading Graph')
    global G
    global Grev
    G, Grev, recLimit = readEdgeList(graphDir)
    print('\n')
    print('   G[1] =',G[0])
    print('   G[4] =',G[3])
    print('   G[-1]=',G[-1])
    sys.setrecursionlimit(recLimit)
    if debug:
        print('\nG = \n',G)
        print('\nGrev = \n',Grev)
    print('\n')
    
    #! DFS on G
    print('-> Two Pass')
    queueList = []
    for i in range((len(G)-1),-1,-1):
        queueList.append(i)
    if debug:
        print('queueList = ',queueList)
    f,leader = DFSLoop(G, queueList)
    if debug:
        print(f)
    print('   G finished')

    #! DFS on Grev
    fSorted = mergeSort(f)
    if debug:
        print(fSorted)
    queueListRev = []
    for i in range((len(f)-1),-1,-1):
        queueListRev.append(fSorted[i][0]-1)
    fRev,leaderRev = DFSLoop(Grev,queueListRev)
    if debug:
        print(leaderRev)
    print('   Grev finished')

    #! store the node acoording to their leader
    index = 0
    leaderBoard = []
    SSC = []
    for leaderIndex in leaderRev:
        if debug:
            print('checking ', leaderIndex)
        if leaderIndex not in leaderBoard:
            leaderBoard.append(leaderIndex)
            SSC.append([index+1])
        else:
            leaderBoardRanking = leaderBoard.index(leaderIndex)
            SSC[leaderBoardRanking].append(index+1)
        index += 1
    if debug:
        print(leaderBoard)
        print(SSC)
    print('   SCC finished')

    return leaderBoard, SSC


if __name__ == '__main__':
    #! for testing
    if len(sys.argv) != 1:
        print('\n')
        leaderBoard, SSC = kosaraju('./SCC_test.txt')
        print('\n')
    
        print(SSC)

    else:
        #! code
        print('\n')
        leaderBoard, SSC = kosaraju('./SCC.txt')
        print('\n')
    
        print(SSC)         


