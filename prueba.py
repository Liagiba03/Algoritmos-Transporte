from queue import PriorityQueue
from BFS import Nodo
def busca_costo_uniforme(nodo_inicial, solucion, mapa_carreteras):
    nodos_frontera = PriorityQueue()
    nodos_frontera.put((0, nodo_inicial))  # La cola con prioridad se ordena por el primer elemento de la tupla
    nodos_visitados = []

    while not nodos_frontera.empty():
        (costo, nodo_actual) = nodos_frontera.get()

        if nodo_actual.get_datos() == solucion:
            return (costo, nodo_actual)

        nodos_visitados.append(nodo_actual)

        for ciudad, costo_camino in mapa_carreteras[nodo_actual.get_datos()].items():
            nodo_hijo = Nodo(ciudad)

            if nodo_hijo not in nodos_visitados:
                nodos_frontera.put((costo + costo_camino, nodo_hijo))

    return None  # No se encontró ninguna solución

# El mapa de carreteras y los costos entre las ciudades
mapa_carreteras = {
    'EDOMEX': {'SLP': 513, 'CDMX': 125},
    'CDMX': {'EDOMEX': 125, 'MICHOACAN': 491, 'SLP': 423},
    'MICHOACAN': {'CDMX': 491, 'SLP': 355, 'MONTERREY': 309, 'SONORA': 346},
    'SONORA': {'MICHOACAN': 346, 'SLP': 603, 'MONTERREY': 296},
    'MONTERREY': {'SONORA': 296, 'MICHOACAN': 346, 'SLP': 313, 'GUADALAJARA': 394},
    'GUADALAJARA': {'MONTERREY': 394, 'SLP': 437},
    'PUEBLA': {'SLP': 514},
    'QUERETARO': {'HIDALGO': 390, 'SLP': 203},
    'HIDALGO': {'QUERETARO': 390, 'SLP': 599},
    'SLP': {'HIDALGO': 599, 'QUERETARO': 203, 'PUEBLA': 514, 'EDOMEX': 513, 'CDMX': 423, 'MICHOACAN': 355, 'SONORA': 603, 'MONTERREY': 313, 'GUADALAJARA': 437}
}

nodo_inicial = Nodo('EDOMEX')
solucion = 'HIDALGO'

resultado = busca_costo_uniforme(nodo_inicial, solucion, mapa_carreteras)

if resultado is not None:
    (costo, nodo_solucion) = resultado
    print(f'El camino más corto desde {nodo_inicial.get_datos()} a {nodo_solucion.get_datos()} tiene un costo de {costo}.')
else:
    print('No se encontró ninguna solución.')