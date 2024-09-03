from BFS import Nodo


def buscar_solucion_UCS (conexiones, estado_inicial, solucion):

    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    #print(nodo_inicial)

    nodo_inicial.set_coste(0)
    #print(nodo_inicial.get_coste())

    nodos_frontera.append(nodo_inicial)
    while (not solucionado) and (len(nodos_frontera) !=0):
        # ordenar la lista de nodos frontera
        nodos_frontera = sorted(nodos_frontera,  key=lambda nodo: Nodo.compara(nodo, nodo_inicial))
        #print("FRONTERA:",[str(n) for n in nodos_frontera])

        #print("VISITADOS:",[str(n) for n in nodos_visitados])
        #nodo = nodos_frontera[0]
        nodo = nodos_frontera.pop(0)
        #print(nodo)
        # extraer nodo y añadirlo a visitados
        #nodos_visitados.append(nodos_frontera.pop(0))
        nodos_visitados.append(nodo)
        #print("VISITADOS:",[str(n) for n in nodos_visitados])
        if nodo.get_datos() == solucion:
            # solución encontrada
            solucionado = True
            return nodo
        else:
            # expandir nodos hijo (ciudades con conexión)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                coste = conexiones[dato_nodo][un_hijo]
                hijo.set_coste(nodo.get_coste() + coste)
                lista_hijos.append(hijo)
                #print("VISITADOS:",[str(n) for n in lista_hijos])
                if not hijo.en_lista(nodos_visitados):
                    # si está en la lista lo suistituimos con el nuevo valor de coste si es menor
                    if not hijo.en_lista(nodos_frontera):
                        nodos_frontera.append(hijo)
                    for n in nodos_frontera:
                        if (n.igual(hijo)) and (n.get_coste() > hijo.get_coste()):
                            nodos_frontera.remove(n)
                            nodos_frontera.append(hijo)
                        else:
                                #nodos_frontera.append(hijo)
                            nodo.set_hijos(lista_hijos)


if __name__ == "__main__":
    conexiones = {
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
    #conexiones = {
    #    '1': {'3':6, '2':3},
    #    '2': {'1':3, '4':1, '3':2},
    #    '3': {'1':6, '2':2, '4':4, '5':2},
    #    '4': {'2':1, '3':4, '5':6},
    #    '5': {'3':2, '4':6, '6':2, '7':2},
    #    '6': {'5':2, '7':3},
    #    '7': {'6':3, '5':2}
    #}

    estado_inicial = 'EDOMEX'
    solucion = 'HIDALGO'

    nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion)
    #MOSTRAR EL RESULTADO
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print('Coste: ' + str(nodo_solucion.get_coste()))
