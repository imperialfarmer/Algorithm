# -*- using: utf-8 -*-
"""
dijkstra algorithm for Path-finding
Solution: 2599,2610,3038,2052,2367,2399,2029,2442,3386,3578
          2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068
"""

import sys
from heapq import *


#! prepare the data
global nodeNum


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
def dijkstra(graph, s, t):
    """
    s: source vertex
    t: target vertex
    """
    # initialize containers
    distQueue = [(0,s,())]
    visited = set()
    track = {s:0}

    while distQueue:
        # get the path with minimum distance so far
        dist_v, v, path = heappop(distQueue)
        if v not in visited:
            visited.add(v)  # mark the node visited
            path = path + (v,) # add v into path
            
            # if the searching reaches the target
            if v == t:
                return (dist_v, path)
            
            # if not, continue searching the neighboured vertex
            for i in range(len(graph[v][0])):
                w = graph[v][0][i]
                if w not in visited:
                    dist_vw = graph[v][1][i]
                    dist_w = dist_v + dist_vw

                    # read the previous distance record from 'track'
                    # will get None if there is no record
                    prevDist_vw = track.get(w, None)
                    # update the recorded distance if the current path is better
                    if prevDist_vw is None or dist_w < prevDist_vw:
                        track[w] = dist_vw
                        heappush(distQueue, (dist_w, w, path))


if __name__ == '__main__':
    print('\n-> Input Data')
    graph = readDirectedEdge('./dijkstraData.txt')
    # print(graph)

    print('-> Searching Shortest Path')
    targets = [7,37,59,82,99,115,133,165,188,197]
    solution = []
    for t in targets:
        dist, path = dijkstra(graph,1,t)
        print('-- TO '+ str(t) + ' --')
        print(dist, path)
        print('\n')
        solution.append(dist)

    print('Final solution')
    print(solution)
    





            
