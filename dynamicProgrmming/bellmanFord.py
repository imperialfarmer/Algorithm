# -*- using:utf-8 -*-
"""
use Bellman-Ford algorithm to compute the shortest path
"""

import sys
import math

class Graph:
    def __init__(self, fileName):
        """
        file format:
        <#vertives> <#edge>
        <tail> <head> <cost>
        """
        print('\n -> Read graph from ', fileName)
        file = open(fileName)
        indexLine = 0
        numVert = 0
        numEdge = 0
        edges = []
        for line in file:
            if indexLine == 0:
                numVert = int(line.split()[0])
                numEdge = int(line.split()[1])
            else:
                tail = int(line.split()[0])
                head = int(line.split()[1])
                cost = int(line.split()[2])
                edges.append( [tail, head, cost] )
            indexLine += 1
        file.close()

        self.numVert = numVert
        self.numEdge = numEdge
        self.edges = edges

        print(' -> Finish')

    def Info(self):
        print('\n -> Geometry info')
        print('    # Vertices = ', str(self.numVert))
        print('    # Edges    = ', str(self.numEdge))
        print('    # Graph')
        for edge in self.edges:
            print('      '+str(edge[0])+'->'+str(edge[1])+':'+str(edge[2]))


class BellmanFord:
    def __init__(self, graph, s):
        """
        find all shortest path starting from s
        """
        print('\n -> Bellman-Ford shortest path algorithm')

        self.hasNegativeCycle = False

        # graph info
        numVert = graph.numVert
        numEdge = graph.numEdge

        # initialize
        # dist[i] = [total cost, from which vertex]
        dist = []
        for i in range(numVert):
            tmp = []
            for j in range(numVert):
                if j == s-1:
                    tmp.append([0, s])
                else:
                    tmp.append([math.inf, 0])
            dist.append(tmp)
        # for i in dist:
        #     print(i)
        #     print()
        

        for i in range(numVert):
            # finding shortest path
            sys.stdout.write('\r -> iteration '+str(i+1)+'/'+str(numVert))
            sys.stdout.flush()
            
            for edge in graph.edges:
                # print(edge)
                w = edge[0]-1
                v = edge[1]-1
                cost_wv = edge[2]

                new_dist = dist[i-1][w][0]+cost_wv
                old_dist = dist[i-1][v][0]

                current_dist = dist[i][v][0]

                # print(str(new_dist)+'?'+str(old_dist))
                # print(str(new_dist)+'?'+str(current_dist))

                if new_dist < old_dist and new_dist < current_dist:
                    dist[i][v] = [new_dist, w+1]
                else:
                    if dist[i][v][1] == 0:
                        dist[i][v] = [min(old_dist, current_dist), dist[i-1][v][1]]
                    else:
                        dist[i][v] = [min(old_dist, current_dist), dist[i][v][1]]

            if i == numVert-1:
                # detecting the negative cycle
                sum = 0
                for vertIndex in range(graph.numVert):
                    sum += dist[i][vertIndex][0] - dist[i-1][vertIndex][0]
                if sum != 0:
                    self.hasNegativeCycle = True
            
            # print(dist[i])
            # input()

        if self.hasNegativeCycle:
            print('\r -> Finish, graph has negative cycle')
        else:
            print('\r -> Finish, graph has no negative cycle')
        self.numVert = numVert
        self.numEdge = numEdge
        self.start = s
        self.dist = dist


    def ShortestPath(self, t, fullPath = False):
        """
        output the value of shortest path from s to t and full path as requested
        """

        print('\n -> Shortest path info')
        if self.hasNegativeCycle:
            print('    Graph is invalid for Bellman-Ford algorithm\n')
        else:
            print('    Lowest cost '+str(self.start)+' -> '+str(t)+' : '+str(self.dist[-1][t-1][0]))
            
            if fullPath:
                path = []
                currentVert = t
                path.append(currentVert)
                while (currentVert != self.start):
                    currentVert = self.dist[-1][currentVert-1][1]
                    path.append(currentVert)
                
                sys.stdout.write('    Shortest path ')
                sys.stdout.flush()
                for i in range(len(path)-1,-1,-1):
                    if path[i] != t:
                        sys.stdout.write(str(path[i])+'->')
                        sys.stdout.flush()
                    else:
                        print(str(path[i]))
                print('\n')

        
if __name__ == '__main__':
    fileNames = ['g1.txt', 'g2.txt', 'g3.txt']
    for file in fileNames:
        print('\n=========================')
        print(' -- Name: '+file+' --\n')
        graph0 = Graph(file)
        # graph0.Info()
        dist0 = BellmanFord(graph0,1)
        dist0.ShortestPath(5,True)
        print(' -- Finish --')
        print('=========================\n')

