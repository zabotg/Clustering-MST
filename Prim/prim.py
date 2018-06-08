# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.

from Utils import graph_to_array
from operator import itemgetter
from Kruskal.union_find import UnionFind
from heapq import heappop, heappush


# Return Prim MST
def prim_mst(graph):
    lista = graph_to_array(graph)
    mstSet = [False] * len(graph)
    heap = []

    heappush(heap, (-1, (0, -1)))  # No escolhido
    mst_complete = []

    while len(heap) > 0:
        poped = heappop(heap)
        node = poped[1][0]
        parent = poped[1][1]

        if mstSet[node] is False:
            mstSet[node] = True
            if parent != -1:
                mst_complete.append((parent, node, poped[0]))

            for node_s in graph[node]:
                dist = graph[node][node_s]
                if mstSet[node_s] is False:
                    heappush(heap, (dist, (node_s, node)))

    return mst_complete


# Return Prim Clusters
def prim_clusters(graph, number_clusters):
    lista = graph_to_array(graph)
    mstSet = [False] * len(graph)
    heap = []

    heappush(heap, (-1, (0, -1)))  # No escolhido
    mst_complete = []

    while len(heap) > 0:
        poped = heappop(heap)
        node = poped[1][0]
        parent = poped[1][1]

        if mstSet[node] is False:
            mstSet[node] = True
            if parent != -1:
                mst_complete.append((parent, node, poped[0]))

            for node_s in graph[node]:
                dist = graph[node][node_s]
                if mstSet[node_s] is False:
                    heappush(heap, (dist, (node_s, node)))

    mst_clustering = sorted(mst_complete, key=itemgetter(2), reverse=True)
    mst_clustering = removeEdges(mst_clustering, number_clusters)

    uf = UnionFind(sorted(graph.keys()))

    for src, dst, weight in mst_clustering:
        if uf.find(src) != uf.find(dst):
            if number_clusters == uf.size: break
            mst_complete.append((src, dst, weight))
            uf.union(src, dst)

    return mst_clustering, [uf.find(i) for i in uf.parent]


# Method to remove edges from MST
def removeEdges(mst_complete, number_clusters):
    mst_clustering = mst_complete
    while number_clusters - 1 > 0:
        mst_clustering.pop(0)
        number_clusters -= 1

    return mst_clustering
