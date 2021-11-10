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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de UFOS
def init():
    analyzer = model.newAnalyzer()
    return analyzer


# Funciones para la carga de datos
def loadData(analyzer, sightingsfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    sightingsfile = cf.data_dir + sightingsfile
    input_file = csv.DictReader(open(sightingsfile, encoding="utf-8"),
                                delimiter=",")
    for ufo in input_file:
        model.addsighting(analyzer, ufo)
    return analyzer
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def lista5(analyzer):
    return model.sublist(analyzer)

def req1(analizer, city):
    return model.req1(analizer, city)

def req2(analizer, duration_min, duration_max):
    return model.req2(analizer,  duration_min, duration_max)

def req3(analizer, lim_inicial, lim_final):
    return model.req3(analizer, lim_inicial, lim_final)

def req4(analyzer, date_min, date_max):
    return model.req4(analyzer,date_min,date_max)
    
def req5(analizer,latitud_min,latitud_max,longitud_min,longitud_max):
    return model.req5(analizer,latitud_min,latitud_max,longitud_min,longitud_max)
    
