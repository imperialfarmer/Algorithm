# -*- using: utf-8 -*-

import random
import numpy as np
import sys

def readAdjacencyList(file):
    adjList = []
    for line in file:
        firstNum = True
        tmpList = []
        for num in line.split():
            if not firstNum:
                tmpList.append(int(num))
            firstNum = False
        adjList.append(tmpList)
    
    return np.array(adjList)


def adjListToEdgeList(adjList):
    edgeList = []
    currentIndex = 1
    for nodeList in adjList:
        for adjcentNode in nodeList:
            pair = [currentIndex, adjcentNode]
            edgeList.append(pair)
        currentIndex += 1
    return np.array(edgeList)


def kargerMinimumCut(adjList, nodeList):
    debug = False

    if debug:
        print(adjList)

    if len(adjList) != 2:
        #! 1. first choose a random edge
        edgeList = adjListToEdgeList(adjList)
        size = len(edgeList)
        chosenIndex = random.randint(0,size-1)
        chosenPair = edgeList[chosenIndex]

        #! 2. merge the nodes on this edge, keep first one and delete the last one
        node0 = min(chosenPair[:])
        node1 = max(chosenPair[:])

        if debug:
            print('Edge is chosen as ' + str(chosenIndex) + ': ' + str(node0) + ' ' + str(node1))
            print('original first line = ',adjList[node0-1])
            print('original end line = ',adjList[node1-1])
        adjList[node0-1].extend(adjList[node1-1][:])
        if debug:
            print('\n')
        adjList = np.delete(adjList,node1-1,axis=0)
        # print(adjList[node0-1])
        for i in range(len(adjList)):
            for j in range(len(adjList[i])):
                if adjList[i][j] == node1:
                    adjList[i][j] = node0
                elif adjList[i][j] > node1:
                    adjList[i][j] -= 1

        #! 3. delete the self-loop
        if debug:
            print('edited first1 line = ',adjList[node0-1])
        newList = []
        for num in adjList[node0-1]:
            if int(num) != node0:
                newList.append(num)
        adjList[node0-1] = newList
        if debug:
            print('edited first2 line = ',adjList[node0-1])
            print(len(adjList))

        #! 4. edit the node index lookup table
        for i in range(len(nodeList)):
            if nodeList[i] == node1:
                nodeList[i] = node0
            elif nodeList[i] > node1:
                nodeList[i] -= 1
            
        adjList, nodeList = kargerMinimumCut(adjList,nodeList)

    return adjList, nodeList


def countCrossingEdges(maxIter, fileName):
    debug = False
    edgeNum = []
    cutList = []
    i = 0
    while i < maxIter:
        adjList = []
        listFile = open(fileName)
        adjList = readAdjacencyList(listFile)
        nodeList = []
        for j in range(len(adjList)):
            nodeList.append(j+1)
        if debug:
            print('original = ', adjList)
        resList, resCut = kargerMinimumCut(adjList,nodeList)
        if debug:
            print('res = ',resList)
            print('num = ',len(resList[0]))
            print('cut = ', resCut)
            print('\n')
        edgeNum.append(len(resList[0]))
        cutList.append(np.array(resCut))
        sys.stdout.write('\r' + '  -> Iteration ' + str(i+1) + '/' + str(maxIter) + ': MIN = ' + str(min(edgeNum[:])))
        sys.stdout.flush()

        i += 1

    return edgeNum, cutList


if __name__ == '__main__':
    # read adjacency
    listFile = open('./kargerMinCut.txt')
    adjList = readAdjacencyList(listFile)
    print('\nCheck the input readings')
    print(adjList[69])
    print('[165, 123, 163, 153, 12, 43, 168, 3, 114, 82, 148, 190, 129, 74, 176, 47, 110, 181, 41, 30]')
    print('----------')
    print(adjList[-1])
    print('[149, 155, 52, 87, 120, 39, 160, 137, 27, 79, 131, 100, 25, 55, 23, 126, 84, 166, 150, 62, 67, 1, 69, 35]')
    print('----------')
    print('Size of Input = ', len(adjList))
    print('----------\n')

    # get the edge list
    edgeList = adjListToEdgeList(adjList)
    print('\nCheck the edge list')
    print(edgeList[0])
    print('[1, 37]')
    print('----------')
    print(edgeList[10])
    print('[1, 78]')
    print('----------')
    print(edgeList[-1])
    print('[200, 35]')
    print('----------')

    # get the minimum cut
    edgeNum, cutList = countCrossingEdges(200, './kargerMinCut.txt')
    print('\n')
    print('Minimum Cut = ', min(edgeNum[:]))
    




