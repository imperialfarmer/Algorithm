# -*- using: utf-8 -*-
"""
dijkstra algorithm for Path-finding
"""

import sys
import heapq


#! prepare the data
global nodeNum
global track
global visited
global distQueue
distQueue = []


def readDirectedEdge(fileName):
    file = open(fileName)
    graph = {}
    count = 1
    for adjLine in file:
        graph[count] = [[],[]]
        for pair in adjLine.split()[1:]:
            nodeIndex = int(pair.split(',')[0])
            weight = int(pair.split(',')[1])
            graph[count][0].append(nodeIndex)
            graph[count][1].append(weight)
        sys.stdout.write('\r   Node ' + str(count))
        sys.stdout.flush()
        count += 1
    file.close()
    print('\n')

    global nodeNum
    nodeNum = count-1

    return graph


#! dijkstra algorithm
def dijkstra(graph, sourceVertex):
    #! mark the node visited
    visited.add(sourceVertex)
    #! calculate the distances from source vertex
    
    for adjNode in graph[sourceVertex][0]:
        if adjNode not in visited:
            dijkstra(graph,adjNode)






if __name__ == '__main__':
    graph = readDirectedEdge('./dijkstraData.txt')

    track = [1000000]*nodeNum
    track[0] = 0
    visited = set()




            
