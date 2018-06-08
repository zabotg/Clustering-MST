# A Python program for Kruskal Minimum Spanning Tree (MST) algorithm.

from Kruskal.union_find import UnionFind
from operator import itemgetter
from Utils import graph_to_array


# Return Kruskal MST
def kruskal_mst(graph):
    lista = graph_to_array(graph)
    lista = sorted(lista, key=itemgetter(2))

    mst_complete = []
    uf = UnionFind(sorted(graph.keys()))

    for src, dst, weight in lista:
        if uf.find(src) != uf.find(dst):
            mst_complete.append((src, dst, weight))
            uf.union(src, dst)
    return mst_complete


# Return Kruskal Clusters
def kruskal_clusters(graph, k):
    lista = graph_to_array(graph)
    lista = sorted(lista, key=itemgetter(2))

    mst_complete = []
    uf = UnionFind(sorted(graph.keys()))

    for src, dst, weight in lista:
        if uf.find(src) != uf.find(dst):
            if k == uf.size: break
            mst_complete.append((src, dst, weight))
            uf.union(src, dst)
    return mst_complete, [uf.find(i) for i in uf.parent]
