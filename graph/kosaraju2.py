# -*- using: utf-8 -*-
"""
An implementation with explanations
Largest five SCCs num: 434821,968,459,313,211
"""

import sys
import operator
from collections import OrderedDict


#! prepare the data
def readEdgeList(fileName):
    file = open(fileName)
    edges = [] # tail -> head
    count = 1
    for line in file:
        edges.append([int(line.split()[0]),int(line.split()[1])])
        sys.stdout.write('\r   Edge '+str(count))
        sys.stdout.flush()
        count += 1
    file.close()
    print(' Finish \n')

    return edges


def buildGraph(edges): 
    """
    the data structure of graph uses dictionary
    key(node index): [finishing time/leader, visited or not, other nodes this node is outgoing to]
    """

    graph = {}
    graphRev = {}
    tail = 0 
    head = 1

    for edge in edges:                                  # First we initialize all nodes for the dictionary
        if edge[tail] not in graph:
            graph[edge[tail]] = [0, False, []]
            graphRev[edge[tail]] = [0, False, []]
        if edge[head] not in graph:                 
            graph[edge[head]] = [0, False, []]
            graphRev[edge[head]] = [0, False, []]

    for edge in edges:                                  # Finally we go through each edge and append
        graph[edge[tail]][2].append(edge[head])         # any connected nodes to our array
        graphRev[edge[head]][2].append(edge[tail])

    return graph, graphRev


#! First pass, to compute the finishing time
t = 0                                   # Here we have "t", which will keep track of finishing times

def DFSPass1(graph, node):

	global t                            # t needs to be global so it can be accessed within every level
	graph[node][1] = True               # we set the boolean to true so we know we've explored this node

	for head in graph[node][2]:          # Here we perform DFS on any non-explored edges
		if not graph[head][1]:           # The DFS explores edges, setting them to "explored" if it finds them
			DFSPass1(graph, head)

	t += 1                              # Here we reset the value of t, and assign it to the current node
	graph[node][0] = t

	return graph


def kosarajuPass1(graph, keys):

    count = 1
    for i in keys:
        if not graph[i][1]:             # Using the boolean values, we perform DFS is a node is unexplored
            graph = DFSPass1(graph, i)
        sys.stdout.write('\r   Vertex '+str(count)+'/'+str(len(graph)))
        sys.stdout.flush()
        count += 1
    print(' Finish \n')

    return graph


#! pass 2, to compute the leader
s = 0                                   # Here we have "s", which will keep track of the leader
leaders = []

def DFSPass2(graph, node):
    global s
    global leaders
    graph[node][1] = True              # This DFS is similar to before, but now we assign leaders
    graph[node][0] = s                  # The first value in the graph dictionary is the leader
	                                    # as opposed to the finishing time, which it was before
    for head in graph[node][2]:
		if not graph[head][1]:
			DFSPass2(graph, head)

    return graph

	
def kosarajuPass2(graph, keys):
    
    global s
    global leaders                      # We can pretty easily keep track of an array of leaders
                                        # We sort the dictionary according to finishing time
    count = 1
    for i in keys:                                  
        if not graph[i][1]:
			s = i                       # For every node, we assign a leader and append it to the
			leaders.append(s)           # leader array
			graph = DFSPass2(graph, i)
        sys.stdout.write('\r   Vertex '+str(count)+'/'+str(len(graph)))
        sys.stdout.flush()
        count += 1
    print(' Finish \n')

    return graph, leaders


def kosaraju(fileName):
    print('\n-- Kosaraju\'s Two Pass Algorithm --\n')

    print('\n-> Reading edge list')
    edges = readEdgeList(fileName)
    graph, graphRev = buildGraph(edges)

    recLimit = len(graph)
    sys.setrecursionlimit(recLimit)

    print('\n-> First pass')
    # Here we sort keys in reverse order so we can start with the largest
    keysRev = list(graphRev.keys())
    keysRev = sorted(keysRev, reverse=True)  
    graphRev = kosarajuPass1(graphRev,keysRev)

    print('\n-> Second pass')
    # Here we sort keys in reverse order acoording to the finishing time in Grev
    graphRevSortedByTime = OrderedDict(sorted(graphRev.items(), key=operator.itemgetter(1), reverse=True))
    keys = list(graphRevSortedByTime.keys())
    graph, leaders = kosarajuPass2(graph,keys)
    return graph, leaders


def groupSCC(graph, leaders):
    group = {}
    for i in range(len(leaders)):
        group[leaders[i]] = [0,[]]
    for i in range(len(graph)):
        group[graph[i+1][0]][1].append(i+1)

    for i in range(len(leaders)):
        group[leaders[i]][0] = len(group[leaders[i]][1])

    return group


if __name__ == '__main__':

    fileName = './SCC.txt'

    # graph is the leader-marked dict
    # leader is the index of leaing vertices
    graph, leaders = kosaraju(fileName)

    group = groupSCC(graph, leaders)
    sortedGroup = sorted(group.items(),key=operator.itemgetter(1), reverse=True)
    SCCnum = []
    for item in sortedGroup:
        SCCnum.append(item[1][0])

    print(SCCnum[:5])


