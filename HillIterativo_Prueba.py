import math
import random

def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 6371.0  # Radio de la Tierra en kilómetros
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat/2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = R * c
    return distancia

def evalua_ruta(ruta, coord):
    total = 0
    for i in range(len(ruta) - 1):
        total += distancia(coord[ruta[i]], coord[ruta[i + 1]])
    total += distancia(coord[ruta[-1]], coord[ruta[0]])  # Cierra el ciclo
    return total

def i_hill_climbing(coord, max_iteraciones=1000):
    ruta = list(coord.keys())
    mejor_ruta = ruta[:]
    random.shuffle(mejor_ruta)
    mejor_distancia = evalua_ruta(mejor_ruta, coord)

    iteraciones = 0
    while iteraciones < max_iteraciones:
        mejora = False
        for i in range(len(ruta) - 1):
            for j in range(i + 1, len(ruta)):
                nueva_ruta = mejor_ruta[:]
                nueva_ruta[i], nueva_ruta[j] = nueva_ruta[j], nueva_ruta[i]
                nueva_distancia = evalua_ruta(nueva_ruta, coord)
                if nueva_distancia < mejor_distancia:
                    mejor_ruta = nueva_ruta[:]
                    mejor_distancia = nueva_distancia
                    mejora = True
                    break
            if mejora:
                break
        if not mejora:
            break
        iteraciones += 1

    return mejor_ruta, mejor_distancia

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
        'QRO': (20.59719437542255, -100.38667040246602),
    }

    ruta, distancia_total = i_hill_climbing(coord)
    print("Ruta:", ruta)
    print("Distancia Total:", distancia_total)
