# -*- using: utf-8 -*-
"""
kosaraju's two pass algorithm is to compute the Strongly Connected Components (SCC)
"""

import sys

def main():
    print('\n-- Kosaraju\'s Two Pass Algorithm --')

    # make a graph and its reverse from the given data
    graph = {}
    graphR = {}

    print('\n-> Reading Graph')
    f = open("./SCC.txt", 'r')
    line = f.readline()
    while line:
        edge = [int(e) for e in line.split()]
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
        if edge[1] in graphR:
            graphR[edge[1]].append(edge[0])
        else:
            graphR[edge[1]] = [edge[0]]
        line = f.readline()
    f.close()
    print('   Finish\n')

    # run depth-first search on graph reverse
    print('-> DFS on Grev')
    node_post = {}
    post_node = {}
    post = 1
    count = 1
    for node in graphR:
        if not (node in node_post):
            prev_dict, prev_index, prev_set = {}, 1, set([node])
            prev_dict[prev_index] = node
            try:
                nodes = graphR[node][:]
            except:
                nodes = []
            next_dict, next_index, next_set = {}, 0, set()
            for n in nodes:
                if not ((n in prev_set) or (n in next_set) or
                        (n in node_post)):
                    next_index += 1
                    next_dict[next_index] = n
                    next_set.add(n)
            while next_dict:
                if next_dict[next_index] in prev_set:
                    next_set.remove(next_dict[next_index])
                    del next_dict[next_index]
                    next_index = len(next_dict)
                else:
                    prev_set.add(next_dict[next_index])
                    prev_index += 1
                    prev_dict[prev_index] = next_dict[next_index]
                    try:
                        nodes = graphR[next_dict[next_index]][:]
                    except:
                        nodes = []
                    next_set.remove(next_dict[next_index])
                    del next_dict[next_index]
                    next_index = len(next_dict)
                    for n in nodes:
                        if not ((n in prev_set) or (n in next_set) or
                                (n in node_post)):
                            next_index += 1
                            next_dict[next_index] = n
                            next_set.add(n)
                    next_index = len(next_dict)
            post = post + len(prev_dict)
            for element in prev_dict:
                if not prev_dict[element] in node_post:
                    node_post[prev_dict[element]] = post - element
                    post_node[post - element] = prev_dict[element]
        sys.stdout.write('\r   Grev '+str(count)+'/'+str(len(graphR)))
        sys.stdout.flush()
        count += 1
    print('   Finish\n')

    # run DFS on graph (by reverse postorder)
    print('-> DFS on G')
    reverse_postorder = post_node.values()[::-1]
    marked = set()
    results = []
    order = 0
    length = len(reverse_postorder)
    while order < length:
        node = reverse_postorder[order]
        if (not (node in marked)):
            prev_dict, prev_index, prev_set = {}, 1, set([node])
            prev_dict[prev_index] = node
            try:
                nodes = graph[node][:]
            except:
                nodes = []
            next_dict, next_index, next_set = {}, 0, set()
            for n in nodes:
                if not ((n in prev_set) or (n in next_set) or (n in marked)):
                    next_index += 1
                    next_dict[next_index] = n
                    next_set.add(n)
            while next_dict:
                if next_dict[next_index] in prev_set:
                    next_set.remove(next_dict[next_index])
                    del next_dict[next_index]
                    next_index = len(next_dict)
                else:
                    prev_set.add(next_dict[next_index])
                    prev_index += 1
                    prev_dict[prev_index] = next_dict[next_index]
                    try:
                        nodes = graph[next_dict[next_index]][:]
                    except:
                        nodes = []
                    next_set.remove(next_dict[next_index])
                    del next_dict[next_index]
                    next_index = len(next_dict)
                    for n in nodes:
                        if not ((n in prev_set) or (n in next_set) or
                                (n in marked)):
                            next_index += 1
                            next_dict[next_index] = n
                            next_set.add(n)
                    next_index = len(next_dict)
            # add the size of the previous strongly connected component
            results.append(len(prev_dict))
        for element in prev_dict:
            marked.add(prev_dict[element])
        sys.stdout.write('\r   G '+str(order+1)+'/'+str(length))
        sys.stdout.flush()
        order += 1
    print('   Finish\n')

    # output the sizes of the 5 largest SCCs in the given graph
    solution = ','.join(str(x) for x in sorted(results + [0] * 5,
                                               reverse=True)[:5])
    print solution


if __name__ == '__main__':
    main()