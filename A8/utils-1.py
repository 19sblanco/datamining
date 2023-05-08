import numpy as np


def power_iteration(M, error, beta):
    M = np.array(M)
    n = len(M)

    r = np.array([1 / n] * n).T
    e = np.array([1] * n)
    A = (beta * M) + (1 - beta) * (1 / n) * e * e.T

    t = 0
    while True:
        t += 1
        r_new = np.dot(A, r)
        if np.linalg.norm(r_new - r) < error:
            break
        r = r_new
    
    return r_new


filename = 'web-Google_10k.txt'
with open(filename,'r') as input_file: 
    # The first 4 lines are metadata about the graph that you do not need 
    # After the metadata, the next lines are edges given in the format: `node1\tnode2\n` where node1 points to node2
    lines = [item.replace('\n','').split('\t') for item in input_file] 
    edges = [[int(item[0]),int(item[1])] for item in lines[4:]]

    nodes_with_duplicates = [node for pair in edges for node in pair]
    nodes = sorted(set(nodes_with_duplicates))

    # There are 10K unique nodes, but the nodes are not numbered from 0 to 10K!!! 
    # E.g. there is a node with the ID 916155 
    # So you might find these dictionaries useful in the rest of the assignment
    node_index = {node: index for index, node in enumerate(nodes)} # given node get index
    index_node = {index: node for node, index in node_index.items()} # given index get node

    # A
    # count outgoing edges from the edge list
    outgoing_edges = [0] * len(nodes)
    for edge in edges:
        index = node_index[edge[0]]
        outgoing_edges[index] += 1

    # B
    # count the number of dead ends in the graph
    dead_ends = []
    for i in range(len(outgoing_edges)):
        if outgoing_edges[i] == 0:
            dead_ends.append(i)


    # constuct M
    M = [[0] * len(nodes) for _ in range(len(nodes))]
    for edge in edges:
        i = node_index[edge[0]]
        j = node_index[edge[1]]
        M[j][i] = 1/outgoing_edges[i]

    # constuct M w/ dead ends
    for i in dead_ends:
        for j in range(len(nodes)):
            M[j][i] = 1/len(nodes)

    r = power_iteration(M, .0001, .85)
    print(r)

    max_val = max(r)
    max_i = r.tolist().index(max_val)
    print("maxval", max_val)
    print("maxi", max_i)

    print("node_id", index_node[max_i])

    # D
    # count incoming edges from the edge list
    incoming_edges = [0] * len(nodes)
    for edge in edges:
        index = node_index[edge[1]]
        incoming_edges[index] += 1
    print("\n")
    print(max(incoming_edges))
    print(incoming_edges[max_i])
    # incoming_edges.sort()
    # print(incoming_edges)

    

