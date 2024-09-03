import math
import random

# Calcular la distancia euclidiana entre dos coordenadas
def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

# Calcular la distancia cubierta por una ruta
def evalua_ruta(ruta, coord):
    total = 0
    for i in range(0, len(ruta) - 1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        total += distancia(coord[ciudad1], coord[ciudad2])
    ciudad1 = ruta[-1] # última ciudad en la ruta
    ciudad2 = ruta[0] # volver a la primera ciudad
    total += distancia(coord[ciudad1], coord[ciudad2])
    return total

# Función para encontrar los nodos más cercanos
def nodos_mas_cercanos(coord, ciudad, k=3):
    distancias = {c: distancia(coord[ciudad], coord[c]) for c in coord if c != ciudad}
    return sorted(distancias, key=distancias.get)[:k]


if __name__ == "__main__":
    coord = {
        'Jiloyork': (19.916012, -99.580580),
        'Toluca': (19.289165, -99.655697),
        'Atlacomulco': (19.799520, -99.873844),
        'Guadalajara': (20.677754472859146, -103.34625354877137),
        'Monterrey': (25.69161110159454, -100.321838480256),
        'QuintanaRoo': (21.163111924844458, -86.80231502121464),
        'Michoacan': (19.701400113725654, -101.20829680213464),
        'Aguascalientes': (21.87641043660486, -102.26438663286967),
        'CDMX': (19.432713075976878, -99.13318344772986),
        'QRO': (20.59719437542255, -100.38667040246602)
    }

    ciudad1 = 'CDMX'
    ciudad2 = 'Monterrey'

    # Encuentra los nodos más cercanos a ciudad1 y ciudad2
    nodos_cercanos1 = nodos_mas_cercanos(coord, ciudad1)
    nodos_cercanos2 = nodos_mas_cercanos(coord, ciudad2)

    # Imprimir nodos seleccionados
    print(f"Nodos cercanos a {ciudad1}: {nodos_cercanos1}")
    print(f"Nodos cercanos a {ciudad2}: {nodos_cercanos2}")

    # Crear ruta inicial con los nodos más cercanos y las ciudades de inicio y fin
    rutaS = [ciudad1] + nodos_cercanos1 + nodos_cercanos2 + [ciudad2]
    rutaS = list(set(rutaS)) # Eliminar duplicados si los hubiera

    # Aplicar recocido simulado
    #rutaS = simulated_annealing(rutaS, coord)
    #distancia_total = evalua_ruta(rutaS, coord)
    print("Ruta:", rutaS)
    #print("Distancia Total:", distancia_total, "km")
