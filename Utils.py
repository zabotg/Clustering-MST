import scipy.spatial.distance as sp
import matplotlib.pyplot as plt
import seaborn as sns

""" Method used to read data file
 Inputs: (file.txt cotaining several vertex)
 -----
 Output: (data containing [x,y] of each vertex)
"""


def read_data_file(input_file=None):
    data = []
    with open(input_file) as file:
        for line in file.readlines():
            point = line.split('\t')
            data.append([float(point[0]), float(point[1])])
    return data


""" Method used to create a complete graph
 Inputs: (data containing [x,y] of each vertex)
 -----
 Output: (adjacency list of a complete graph)
"""


def create_complete_graph(data):
    graph = {}
    for src in range(0, len(data)):
        for dst in range(0, len(data)):
            if src == dst: continue
            if dst > src: break
            if src not in graph:
                graph[src] = {}
            if dst not in graph:
                graph[dst] = {}
            peso = sp.euclidean(data[src], data[dst])
            graph[dst][src] = peso
            graph[src][dst] = peso

    return graph


""" Method used to transform a adjacency list in array
 Inputs: (adjacency list of a complete graph)
 -----
 Output: (list of complete graph)
"""


def graph_to_array(graph):
    lista = []
    for src in graph:
        for dst in graph[src]:
            aresta = (src, dst, graph[src][dst])
            lista.append(aresta)
    return lista


""" Method used to plot Minimum Spanning Tree (MST)
 Inputs: (data containing [x,y] of each vertex, list of edges)
 -----
 Output: (plot MST with vertex linked edges)
"""


def plot_mst(data, edges):
    for edge in edges:
        src = edge[0]  # src
        dst = edge[1]

        xs = (data[src][0], data[dst][0])
        ys = (data[src][1], data[dst][1])
        plt.plot(xs, ys, ls='-', color='purple')

    for x, y in data:
        plt.plot(x, y, marker='.', mec='black', mfc='black')
        plt.show()


""" Method used to plot clusters
 Inputs: (data containing [x,y] of each vertex, list clusters)
 -----
 Output: (plot clusters with different colors)
"""


def plot_clusters(data, clusters):
    idx = list(set(clusters))
    palette = sns.color_palette(None, len(idx))

    i = 0;
    for x, y in data:
        plt.scatter(x, y, marker='.', color=palette[idx.index(clusters[i])])
        i += 1
    plt.show()


""" Method used to write the output file
 Inputs: (List of clusters, output path)
 -----
 Output: (File with clusters)
"""


def write_archive(clusters, output):
    arq = open(output, 'w')
    for i in clusters:
        arq.write(str(i))
        arq.write('\n')
    arq.close()
