# Projeto - Agrupamento

Este projeto foi desenvolvido com o objetivo de implementar dois algoritmos de Árvores Geradoras Mínimas (*Mínimum Spanning Tree* - MST), *Prim* e *Kruskal*, a fim de encontrar um agrupamento em uma base de dados sintética proposta no trabalho de [(Gionis, Heikki e Tsaparas, 2007)](http://users.ics.aalto.fi/gionis/ca.pdf).

O agrupamento (*clustering*) consiste em separar objetos em grupos, baseando-se nas características que estes possuem. A ideia básica consite em colocar em um mesmo grupo, objetos que sejam similares de acordo com algum critério pré-determinado. O critério utilizado neste trabalho é uma distância, calculada a partir de uma função Euclidiana.

## Execução
```python
 $ python clustering.py input_file output_file algorithm number_clusters
 ```
 onde:
 * **input_file**: Path do arquivo de entrada contendo todos os vértice do grafo no formato (x, y).
 * **output_file**: Path do arquivo de saída
 * **algorithm**: Uma *string* indicando qual algoritmo deve ser executado:
    + **prim**: Algoritimo de Prim
    + **kruskal**: Algoritmo de Kruskal
 * **number_clusters** : Um número inteiro *k*, indicando o número de grupos a serem formados
 
## Resultados Finais
<p align="center">
  <img src="https://github.com/zabotg/Clusterizacao-MST/blob/master/MST-Completa.png" width="287"/>
  <img src="https://github.com/zabotg/Clusterizacao-MST/blob/master/MST-Clusterizada.png" width="287"/>
  <img src="https://github.com/zabotg/Clusterizacao-MST/blob/master/Clusters.png" width="287"/>
</p>
