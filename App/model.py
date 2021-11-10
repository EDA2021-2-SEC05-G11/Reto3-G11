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
from DISClib.Algorithms.Sorting import mergesort as ms
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

# Req 1

def req1(cont, ciudad):

    cont["city"]= om.newMap(omaptype='BST', comparefunction= comparecity)
    diccionario={}
    contenido ={}
    for i in range(1, lt.size(cont['Sightings']) +1):
        contenido ={}
        ufo = lt.getElement(cont['Sightings'], i)
        city = ufo["city"] 

        contenido["datetime"] = ufo["datetime"]
        contenido["city"] = ufo["city"]
        contenido["state"] = ufo["state"]
        contenido["country"] =  ufo["country"] 
        contenido["shape"] =  ufo["shape"] 
        contenido["duration (seconds)"] = ufo["duration (seconds)"] 

        if city in diccionario:
            lt.addLast(diccionario[city], contenido)
        else:
            diccionario[city]=lt.newList('ARRAY_LIST')
            lt.addLast(diccionario[city], contenido)

    for i in diccionario.keys():

        orden=ms.sort(diccionario[i], comparaciondatetime)
        om.put(cont["city"], i, orden)

    print("existen avistamientos en " + str(om.size(cont['city'])) + " ciudades diferentes." )
    final = om.get(cont["city"], ciudad)
    print("Existen " + str(final["value"]["size"]) + " avistamientos en la ciudad de " + ciudad)

    return   print(final["value"]["elements"][:3] + final["value"]["elements"][-3:])

def comparecity(city1, city2):

    """
    Compara dos tipos de ciudades en formato (str)
    """
    if (city1 == city2):
        return 0
    elif (city1 < city2):
        return 1
    else:
        return -1

def comparaciondatetime(e1,e2):

    """
    Compara dos fechas en formato (AA/DD/MM HH:MM:SS)
    """

    e1=datetime.datetime.strptime(e1["datetime"], '%Y-%m-%d %H:%M:%S')
    e2=datetime.datetime.strptime(e2["datetime"], '%Y-%m-%d %H:%M:%S')

    return e1 < e2   

def req3(cont, lim_inicial, lim_final):

    inicial= datetime.datetime.strptime(lim_inicial, '%Y-%m-%d, %H:%M:%S')
    final= datetime.datetime.strptime(lim_final, '%Y-%m-%d, %H:%M:%S')
    limite_inicial = inicial.time()
    limite_final = final.time()
    final = lt.newList('ARRAY_LIST')

    cont["hora"]= om.newMap(omaptype='BST', comparefunction= comparehora)
    diccionario={}
    contenido= {}
    for i in range(1, lt.size(cont['Sightings']) +1):
        contenido={}
        ufo = lt.getElement(cont['Sightings'], i)
        fecha = datetime.datetime.strptime(ufo["datetime"], '%Y-%m-%d %H:%M:%S')
        hora = fecha.time()

        contenido["datetime"] = ufo["datetime"]
        contenido["city"] = ufo["city"]
        contenido["state"] = ufo["state"]
        contenido["country"] =  ufo["country"] 
        contenido["shape"] =  ufo["shape"] 
        contenido["duration (seconds)"] = ufo["duration (seconds)"] 

        if hora >= limite_inicial and hora <= limite_final:

            lt.addLast(final, contenido)

        if hora in diccionario:

            lt.addLast(diccionario[hora], contenido)

        else:
            diccionario[hora]=lt.newList('ARRAY_LIST')
            lt.addLast(diccionario[hora], contenido)
    fin = ms.sort(final, compareh)
    ini = lt.subList(fin, 1, 3)
    fini = lt.subList(fin, -3, 3)

    for i in diccionario.keys():

        orden=ms.sort(diccionario[i], comparaciondatetime)
        om.put(cont["hora"], i, orden)

    print("Existen " + str(om.size(cont['hora'])) + " avistamientos con diferentes horas. ")
    print("La ultima hora que se registro un avistamiento fue a las "+ str(om.maxKey(cont['hora'])))
    print("Se encontraron " + str(lt.size(fin)) + " avistamientos dentro del rango dado")

    for i in range(1, lt.size(fini)+1):
        lt.addLast((ini), lt.getElement(fini, i))

    return print(ini)

def comparehora(hora1, hora2):

    """
    Compara dos tipos de hora
    """
    if (hora1 == hora2):
        return 0
    elif (hora1 > hora2):
        return 1
    else:
        return -1

def compareh(hora1, hora2):

    """
    Compara dos horas en formato %H:%M:%S
    """

    e1=datetime.datetime.strptime(hora1["datetime"], '%Y-%m-%d %H:%M:%S')
    e2=datetime.datetime.strptime(hora2["datetime"], '%Y-%m-%d %H:%M:%S')

    return e1.time() < e2.time()

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
