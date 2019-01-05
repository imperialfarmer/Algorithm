# -*- using: utf-8 -*-
"""
The implementation concumes too much memory
when programing recursive, think of how to use memory carefully
"""

import sys
from mergeSort import mergeSort


fileName = './SCC_test.txt'

#! read data
def readEdgeList(fileName):
    debug = False
    file = open(fileName)
    edgeList = [] # tail -> head
    count = 1
    # convert the edge list to vertices list
    # in vertices list, the head vertex from this vertex is recorded
    nodeList = []
    tmp = []
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
                print(nodeList)
            tmp = []
            nodeCount += 1
            while nodeCount != int(line.split()[0]):
                nodeCount += 1
                nodeList.append([])
            tmp.append(int(line.split()[1]))

        sys.stdout.write('\r   Edge '+str(count)+' Vertex '+str(nodeCount))
        sys.stdout.flush()
        count += 1
    nodeList.append(tmp)
    file.close()

    # offsetList = []
    # offsetList.append(0)
    # offset = 0
    # print(nodeList)
    # for nums in nodeList:
    #     offsetList.append(len(nums)+offsetList[offset])
    #     offset += 1
    # print(offsetList)
    
    print('\n')
    print('   Readjust missed nodes')
    maxNum = len(nodeList)
    print('   Current max = '+str(maxNum)+' max in list = '+str(maxIndex))
    while  maxNum < maxIndex:
        nodeList.append([])
        maxNum += 1
    print('   Now total node num = ', maxNum)
    
    nodeListRev = []
    for i in range(len(nodeList)):
        nodeListRev.append([])
    
    count = 1
    for pair in edgeList:
        head = pair[0]
        tail = pair[1]
        nodeListRev[tail-1].append(head)
        sys.stdout.write('\r   Grev Edge '+str(count)+'/'+str(len(edgeList))+' generated')
        sys.stdout.flush()
        count += 1

    return nodeList, nodeListRev, (len(nodeList)+len(edgeList))*100

#! read input
print('-> Reading Graph')
global G
global Grev
G, Grev, recLimit = readEdgeList(fileName)
sys.setrecursionlimit(recLimit)

print('\n')
# print('   G[1] =',G[0])
# print('   G[4] =',G[3])
# print('   G[-1]=',G[-1])
# print('\n')

global visited
visited = []
global f
f = []
global leader
leader = []
global nodeNum
nodeNum = len(G)
for i in range(nodeNum):
    visited.append(False)
    f.append([i+1,-1])
    leader.append(-1)


#! graph algorithms
def DFSLoop(queueList):
    #! initialize parameters
    global t
    t = 0
    global s
    s = 0

    global nodeNum

    #! loop through the graph using DFS
    index = 1
    for i in queueList:
        if not visited[i]:
            s = i+1
            DFS(i)
        sys.stdout.write('\r   Finish '+str(index)+'/'+str(nodeNum))
        sys.stdout.flush()
        index += 1

    return f, leader


def DFS(i):
    debug = False
    global t
    global s
    global leader

    links = G[i]
    if debug:
        print('time = ', t)
    visited[i] = True
    leader[i] = s
    if debug:
        print(links)
    if len(links) >= 1:
        for headIndex in links:
            if not visited[headIndex-1]:
                if debug:
                    print(str(i+1) + '->' + str(headIndex))
                DFS(headIndex-1)
    t += 1
    f[i][1] = t
    if debug:
        print('f('+str(i+1)+')='+str(t))
        print('leader('+str(i+1)+')='+str(leader[i]))


def kosaraju():
    print('-- Kosaraju\'s Two Pass Algorithm --')
    debug = False
    global G
    global Grev
    
    #! DFS on G
    print('-> Two Pass')
    queueList = []
    for i in range((len(G)-1),-1,-1):
        queueList.append(i)
    if debug:
        print('queueList = ',queueList)
    DFSLoop(queueList)
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
    G = Grev
    for i in range(len(G)):
        visited[i] = False
        f[i] = [i+1,-1]
        leader[i] = -1
    DFSLoop(queueListRev)
    if debug:
        print(leader)
    print('   Grev finished')

    #! store the node acoording to their leader
    index = 0
    leaderBoard = []
    SSC = []
    for leaderIndex in leader:
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


print('\n')
leaderBoard, SSC = kosaraju()
print('\n')

print(SSC)
clusterNum = []
for nums in SSC:
    clusterNum.append(len(nums))
sortedClusterNum = sorted(clusterNum,key=int,reverse=True)
print(sortedClusterNum[:5])


