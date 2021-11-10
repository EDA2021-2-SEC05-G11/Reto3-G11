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


from DISClib.DataStructures.bst import maxKey
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as me
from DISClib.ADT import orderedmap as om
from DISClib.Algorithms.Sorting import mergesort as ms
import datetime
assert cf
from prettytable import PrettyTable
import prettytable

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


#Req2
#Funciones de comparación
def compareCitys(ufo1, ufo2):
        return (str(ufo1['city']) < str(ufo2['city']))

def compareduration(ufo1, ufo2):
        return (float(ufo1['duration (seconds)']) < float(ufo2['duration (seconds)']))

def req2(cont, duration_min, duration_max):
    cont["duration"]= om.newMap(omaptype='BST', comparefunction= compareDuration)
    diccionario={}
    for i in range(1, lt.size(cont['Sightings']) +1):
        ufo = lt.getElement(cont['Sightings'], i)
        duracion = float(ufo["duration (seconds)"])

        if duracion in diccionario:
            diccionario[duracion].append(ufo)
        else:
            diccionario[duracion]=[ufo]

    for i in diccionario.keys():

        om.put(cont["duration"], i, diccionario[i])


    #Liberar elementos dentro de listas y dejarlos como uno solo
    Listas=[]
    Lista=(om.values(cont['duration'],duration_min,duration_max+1))
    for i in lt.iterator(Lista):
        if type(i)==list:
            for j in i:
                Listas.append(j)
        elif type(i)!=list:
            Listas.append(i)
    
    #Ordenamiento y finalización
    Lista_sort=lt.newList(datastructure='ARRAY_LIST',cmpfunction=compareCitys)
                  #Eliminacion de info innecesaria
    """
    for i in Listas:
        [i.pop(key) for key in ['latitude', 'longitude','duration (hours/min)','date posted','comments']]
    """

    for i in Listas:
        lt.addLast(Lista_sort,i)
   
    sorted_list = me.sort(Lista_sort, compareCitys)
    sorted_list_1 = me.sort(sorted_list, compareduration)
    list_primeros= lt.subList(sorted_list_1,1,3)
    list_ultimos= lt.subList(sorted_list_1,-2,3)
    lista_final= lt.newList(datastructure='ARRAY_LIST')
    for i in lt.iterator(list_primeros):
        lt.addLast(lista_final,i)
    for i in lt.iterator(list_ultimos):
        lt.addLast(lista_final,i)
    print()
    print("Existen "+str(lt.size(om.keySet(cont['duration'])))+ " duraciones diferentes de UFO sightings.")
    print()
    print("La duracion mas larga de UFO sightings es: "+str(om.maxKey(cont['duration']))+" segundos.")
    print()
    print("Existen "+str(len(Listas))+" avistamientos entre: "+str(duration_min)+" y "+str(duration_max)+" segundos de duración.")
    print()
    print("Los primero 3 y ultimos 3 avistamientos en la duración dada son: ")
    print()
    print(lista_final)
    
    
    
        
def compareDuration(duration1, duration2):

    """
    Compara dos tipos de ciudades
    """
    if (duration1 == duration2):
        return 0
    elif (duration1 > duration2):
        return 1
    else:
        return -1

def compareCity_(city1,city2):
    
    if (city1 == city2):
        return 0
    elif (city1 > city2):
        return 1
    else:
        return -1

#Req 3
def compareTime(time1, time2):
    """
    Compara dos fechas
    """
    if (time1 == time2):
        return 0
    elif (time1 > time2):
        return 1
    else:
        return -1
def compareDateTime(ufo1, ufo2):
   return ufo1['datetime'] < ufo2['datetime']

def compareTime_(ufo1, ufo2):
   return ufo1['time'] < ufo2['time']



def req4(cont, hora_min, hora_max):
    cont["Time"]= om.newMap(omaptype='BST', comparefunction= compareTime)
    diccionario={}
    for i in range(1, lt.size(cont['Sightings']) +1):
        ufo = lt.getElement(cont['Sightings'], i)

        fecha = (str(ufo['datetime'])[-8:])
                
        ufo['datetime']= datetime.datetime.strptime(ufo['datetime'], '%Y-%m-%d %H:%M:%S')
        fecha_ufo= datetime.datetime.strptime(fecha, '%H:%M:%S').time()
        ufo['time'] = (str(fecha_ufo)[-8:])
        if fecha_ufo in diccionario:
            diccionario[fecha_ufo].append(ufo)
        else:
            diccionario[fecha_ufo]=[ufo]

    for i in diccionario.keys():
        om.put(cont["Time"], i, diccionario[i])
    
    #Liberar elementos dentro de listas y dejarlos como uno solo
    Listas=[]
    Lista=(om.values(cont['Time'],hora_min,hora_max))
    
    for i in lt.iterator(Lista):
        if type(i)==list:
            for j in i:
                Listas.append(j)
        elif type(i)!=list:
            Listas.append(i)
    
    #Ordenamiento y finalización
    Lista_sort=lt.newList(datastructure='ARRAY_LIST',cmpfunction=compareTime_)
                          #Eliminacion de info innecesaria
    """
    for i in Listas:
        [i.pop(key) for key in ['latitude', 'longitude','duration (hours/min)','date posted','comments']]
    """
        
    for i in Listas:
        i['datetime'] = str(i['datetime'])
        lt.addLast(Lista_sort,i)
    
    sorted_list_1 = me.sort(Lista_sort, compareTime_)
    list_primeros= lt.subList(sorted_list_1,1,3)
    
    
    list_ultimos= lt.subList(sorted_list_1,-2,3)
    lista_final= lt.newList(datastructure='ARRAY_LIST',cmpfunction=compareDateTime)
    for i in lt.iterator(list_primeros):
        lt.addLast(lista_final,i)
    for i in lt.iterator(list_ultimos):
        lt.addLast(lista_final,i)

    print()
    print("Hay "+str(lt.size(om.keySet(cont['Time'])))+" avistamientos de ovnis con diferentes horarios [hh:mm:ss].")
    print()
    print("La hora de avistamiento de ovni mas tarde es a las: "+str(om.maxKey(cont['Time'])))
    print()
    print("Existen "+str(len(Listas))+" avistamientos entre las horas: "+str(hora_min)+" y "+str(hora_max))
    print()
    print("Los primeros 3 y ultimos 3 avistamientos de ovnis en este rango de horas son: ")
    print()
    print(lista_final)

#Req5
def req5(cont,latitud_min,latitud_max,longitud_min,longitud_max):
    #BST por latitud en general
    cont["latitud"]= om.newMap(omaptype='BST', comparefunction= compareTime)
    diccionario={}
    
    for i in range(1, lt.size(cont['Sightings']) +1):
        ufo = lt.getElement(cont['Sightings'], i)
        latitud = round(float(ufo['latitude']),2)
        if latitud in diccionario:
            diccionario[latitud].append(ufo)
        else:
            diccionario[latitud]=[ufo]

    for i in diccionario.keys():
        om.put(cont["latitud"], i, diccionario[i])

    #BST por longitud en general
    cont["longitud"]= om.newMap(omaptype='BST', comparefunction= compareTime)
    diccionario={}
    for i in range(1, lt.size(cont['Sightings']) +1):
        ufo = lt.getElement(cont['Sightings'], i)
        longitud = round(float(ufo['longitude']),2)
        if longitud in diccionario:
            diccionario[longitud].append(ufo)
        else:
            diccionario[longitud]=[ufo]

    for i in diccionario.keys():
        om.put(cont["longitud"], i, diccionario[i])

    
     #BST por rango de latitud
    cont["ran_lat"]= om.newMap(omaptype='BST', comparefunction= compareTime)
    Listas=[]
    valores_lat = om.values(cont['latitud'],latitud_min,latitud_max)
    
    for i in lt.iterator(valores_lat):
        if type(i)==list:
            for j in i:
                Listas.append(j)
        elif type(i)!=list:
            Listas.append(i)
    for i in Listas:
        [i.pop(key) for key in ['duration (hours/min)','date posted','comments']]
    
    Lista_=lt.newList(datastructure='ARRAY_LIST')
    for i in lt.iterator(valores_lat):
        lt.addLast(Lista_,i[0])
    
    diccionario={}
    for i in range(1, lt.size(Lista_) +1):
        ufo = lt.getElement(Lista_, i)
        latitud = round(float(ufo['latitude']),2)
        if latitud in diccionario:
            diccionario[latitud].append(ufo)
        else:
            diccionario[latitud]=[ufo]

    for i in diccionario.keys():
        om.put(cont["ran_lat"], i, diccionario[i])
    
      #BST por longitud por parametro
    cont["ran_lon"]= om.newMap(omaptype='BST', comparefunction= compareTime)
    
    valores_lon_lat = om.values(cont['longitud'],longitud_max,longitud_min)
    
    Lista_=lt.newList(datastructure='ARRAY_LIST')
    for i in lt.iterator(valores_lon_lat):
        lt.addLast(Lista_,i[0])
    
    diccionario={}
    for i in range(1, lt.size(Lista_) +1):
        ufo = lt.getElement(Lista_, i)
        longitud = round(float(ufo['longitude']),2)
        if longitud in diccionario:
            diccionario[longitud].append(ufo)
        else:
            diccionario[longitud]=[ufo]

    for i in diccionario.keys():
        om.put(cont["ran_lon"], i, diccionario[i])
    keys= om.keySet(cont['ran_lon'])

    lista_final_ = lt.newList(datastructure='ARRAY_LIST')
    for j in lt.iterator(keys):
        ufo_= om.get(cont['ran_lon'],j)
        lt.addLast(lista_final_,ufo_)
    
    list_primeros= lt.subList(lista_final_,1,3)
    list_ultimos= lt.subList(lista_final_,-2,3)
    lista_final= lt.newList(datastructure='ARRAY_LIST',cmpfunction=compareDateTime)
    for i in lt.iterator(list_primeros):
        lt.addLast(lista_final,i)
    for i in lt.iterator(list_ultimos):
        lt.addLast(lista_final,i)
    
    Lista_ultimo=lt.newList(datastructure='ARRAY_LIST')
    for i in (lista_final['elements']):
        for j in i['value']:
            lt.addLast(Lista_ultimo,j)
    Listas=[]
    for i in lt.iterator(Lista_ultimo):
        if type(i)==list:
            for j in i:
                Listas.append(j)
        elif type(i)!=list:
            Listas.append(i)

    for i in Listas:
        for j in i.copy().keys():
            if j=='duration (hours/min)' or j=='date posted' or j=='comments':
                del(i[j])
    
    print()
    print("Existen "+str(lt.size(Lista_ultimo))+" avistamientos en el área dada.")
    print()
    print("Los primeros 5 y ultimos 5 avistamientos son: ")
    print()
    print(Lista_ultimo)
    
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
