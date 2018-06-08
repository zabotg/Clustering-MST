#    Copyright (C) 2017-2018 by
#    Guilherme Zabot <zabot.gui@gmail.com>
#    All rights reserved.

from Utils import *
from Kruskal.kruskal import *
from Prim.prim import *

import sys


def main():
    path_input = sys.argv[1]
    path_output = sys.argv[2]
    algorithm = str(sys.argv[3]).lower()
    number_clusters = int(sys.argv[4])

    data = read_data_file(path_input)
    graph = create_complete_graph(data)

    if algorithm == 'kruskal':
        edges, clusters = kruskal_clusters(graph, number_clusters)

    if algorithm == 'prim':
        edges, clusters = prim_clusters(graph, number_clusters)

    write_archive(clusters, path_output)


if __name__ == "__main__":
    main()
