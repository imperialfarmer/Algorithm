# -*- using:utf-8 -*-
"""
Solution = -3612829
"""

import sys

def ReadEdge(fileName):
    file = open(fileName)
    i = 0
    edges = {}
    nodes = {}
    numNode = 0
    numEdge = 0
    for line in file:
        if i == 0:
            numNode = int(line.split()[0])
            numEdge = int(line.split()[1])
            for j in range(numNode):
                nodes[j+1] = []
        else:
            node1 = int(line.split()[0])
            node2 = int(line.split()[1])
            weight = int(line.split()[2])
            edges[i] = [node1, node2, weight]
            nodes[node1].append([i,node2])
            nodes[node2].append([i,node1])

        i += 1

    return edges, nodes


def brute(edges,nodes):
    V = set()
    for i in range(1,len(nodes)+1):
        V.add(i)
    X = set()
    candidate = 1
    T = []
    sumCost = 0
    while len(V) > 1:
        # sys.stdout.write('\r'+str(len(V))+' Remain     ')
        # sys.stdout.flush()
        V.remove(candidate)
        X.add(candidate)
        min = 1000000000000000000000000
        minEdge = 0
        for v in X:
            # print('v = ', v)
            for w in nodes[v]:
                # print('w = ', w)
                # print('w[1] = ', w[1])
                if w[1] in V:
                    e = w[0]
                    cost = edges[e][2]
                    # print('cost = ', cost)
                    if cost < min:
                        min = cost
                        candidate = w[1]
                        minEdge = e
                        # print(v)
        sumCost += min
        # print('candidate = ', candidate)
        # print('min cost = ', min)
        # print('total cost = ', sumCost)
        T.append(minEdge)
        # input(' ')
    print('\n')

    return T, sumCost


if __name__ == '__main__':
    edges, nodes = ReadEdge('./edges.txt')

    T, sumCost = brute(edges,nodes)
    print('Brute = ', sumCost)

    # 1: [[1, 2], [500, 132], [501, 171], [502, 244], [503, 310], [504, 316], [505, 324], [506, 397], [507, 414]]

