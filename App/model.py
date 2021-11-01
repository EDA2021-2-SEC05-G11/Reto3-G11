"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():
    analyzer = {'Sightings': None
                }

    analyzer['Sightings'] = lt.newList('ARRAY_LIST')
    
    return analyzer

# Funciones para agregar informacion al catalogo
def addsighting(analyzer, ufo):
    lt.addLast(analyzer['Sightings'], ufo)
    return analyzer
# Funciones para creacion de datos
def sublist(analyzer):
    Lista_5_primeros = lt.subList(analyzer['Sightings'], 1, 5)
    Lista_5_ultimos = lt.subList(analyzer['Sightings'], -4, 5)
    return Lista_5_primeros, Lista_5_ultimos

def req1(cont, ciudad):

    cont["city"]= om.newMap(omaptype='BST', comparefunction= comparecity)
    diccionario={}
    for i in range(1, lt.size(cont['Sightings']) +1):
        ufo = lt.getElement(cont['Sightings'], i)
        city = ufo["city"]  

        if city in diccionario:
            diccionario[city].append(ufo)
        else:
            diccionario[city]=[ufo]

    for i in diccionario.keys():

        om.put(cont["city"], i, diccionario[i])

    print(om.size(cont['city']))
    final = om.get(cont["city"], ciudad)
    return print(final["value"])

def comparecity(city1, city2):

    """
    Compara dos tipos de ciudades
    """
    if (city1 == city2):
        return 0
    elif (city1 > city2):
        return 1
    else:
        return -1

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
