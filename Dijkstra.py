import sys

# Função do algoritmo de Dijkstra
def calcular_dijkstra(grafo, origem):

  # Inicialização das distâncias com infinito, exceto a origem que é zero
  distancias = {v: sys.maxsize for v in grafo}
  distancias[origem] = 0

  # Conjunto de vértices visitados
  visitados = set()

  while visitados != set(distancias):
      # Encontra o vértice não visitado com menor distância atual
      vertice_atual = None
      menor_distancia = sys.maxsize
      for v in grafo:
          if v not in visitados and distancias[v] < menor_distancia:
              vertice_atual = v
              menor_distancia = distancias[v]

      # Marca o vértice atual como visitado
      visitados.add(vertice_atual)

      # Atualiza as distâncias dos vértices vizinhos
      for vizinho, peso in grafo[vertice_atual].items():
          if distancias[vertice_atual] + peso < distancias[vizinho]:
              distancias[vizinho] = distancias[vertice_atual] + peso

  # Retorna as distâncias mais curtas a partir da origem
  return distancias

# Definindo o grafo com as conexões e custos
grafo = {
    '1': {'3':6, '2':3},
    '2': {'1':3, '4':1, '3':2},
    '3': {'1':6, '2':2, '4':4, '5':2},
    '4': {'2':1, '3':4, '5':6},
    '5': {'3':2, '4':6, '6':2, '7':2},
    '6': {'5':2, '7':3},
    '7': {'6':3, '5':2}
}

# Ponto de partida
origem = '1'

# Chamando o algoritmo de Dijkstra para encontrar os caminhos mais curtos a partir de A
caminhos_mais_curto = calcular_dijkstra(grafo, origem)

# Exibindo os caminhos mais curtos
for destino, distancia in caminhos_mais_curto.items():
  print(f"Caminho mais curto de {origem} para {destino}: {distancia}")