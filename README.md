# Projeto - Agrupamento

Este projeto foi desenvolvido com o objetivo de implementar dois algoritmos de Árvores Geradoras Mínimas (*Mínimum Spanning Tree* - MST), *Prim* e *Kruskal*, a fim de encontrar um agrupamento em uma base de dados sintética proposta no trabalho de [(Gionis, Heikki e Tsaparas, 2007)](http://users.ics.aalto.fi/gionis/ca.pdf).

O agrupamento, ou *clustering* consiste em separar objetos em grupos, baseando-se nas características que estes possuem. A ideia básica consite em colocar em um mesmo grupo, objetos que sejam similares de acordo com algum critério pré-determinado. O critério utilizado neste trabalho é uma distância, calculada a partir de uma função Euclidiana.

## Instalação

## Execução
"python clustering.py x1, x2, x3, x4"

## Resultados Finais
<p align="center">
  <img src="https://github.com/zabotg/Clusterizacao-MST/blob/master/MST-Completa.png" width="287"/>
  <img src="https://github.com/zabotg/Clusterizacao-MST/blob/master/MST-Clusterizada.png" width="287"/>
  <img src="https://github.com/zabotg/Clusterizacao-MST/blob/master/Clusters.png" width="287"/>
</p>


MUDAR A FUNÇÃO DE LEITURA PARA 
```python
  lines = list(open('data.txt', 'r'))
 ```
