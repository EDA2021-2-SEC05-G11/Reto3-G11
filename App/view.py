"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import datetime


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


sightingsfile = 'UFOS//UFOS-utf8-small.csv'
cont = None

def printMenu():
    print("Bienvenido")
    print("A- Inicializar analizador.")
    print("B- Cargar información de crimenes.")
    print("1- Contar los avistamientos en una ciudad.")
    print("2- Contar los avistamientos por duración. ")
    print("3- Contar avistamientos por Hora/Minutos del día. ")
    print("4- Contar los avistamientos en un rango de fechas ")
    print("5- Contar los avistamientos de una Zona Geográfica. ")
    print("0- Salir")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if str(inputs[0]).lower() == "a":
        print("Cargando información de los archivos ....")
        cont = controller.init()
    elif str(inputs[0]).lower() == "b":
        print("\nCargando información de avistamientos ....")
        controller.loadData(cont, sightingsfile)
        print('Se encontraron: ' + str(lt.size(cont['Sightings']))+" avistamientos.")
        print()
        print("Los primero y ultimos 5 avistamientos son: ")
        print()
        print(controller.lista5(cont))

    elif int(inputs[0]) == 1:
        ciudad = str(input("Ingrese el nombre de la ciudad a consultar: \n"))
        controller.req1(cont, ciudad)

    elif int(inputs[0]) == 2:
        duration_min = float(input("Ingrese la duracion minima: "))
        duration_max = float(input("Ingrese la duracion maxima: "))
        controller.req2(cont, duration_min, duration_max)

    elif int(inputs[0]) == 3:
        lim_inicial = "2000-01-01, " + str(input("Ingrese el limite inicial de la hora: \n"))
        lim_final = "2000-01-01, " + str(input("Ingrese el limite final de la hora: \n"))
        controller.req3(cont, lim_inicial, lim_final)
   
    elif int(inputs[0]) == 4:
        date_min = str(input("Digite la fecha minima: "))
        date_min = datetime.datetime.strptime(date_min, '%Y-%m-%d' )
        date_max = str(input("Digite la fecha máxima: "))
        date_max = datetime.datetime.strptime(date_max, '%Y-%m-%d' )
        controller.req4(cont, date_min,date_max)

    elif int(inputs[0]) == 5:
        latitud_min = float(input("Digite la latitud minima: "))
        latitud_max = float(input("Digite la latitud maxima: "))
        longitud_min = float(input("Digite la longitud minima: "))
        longitud_max = float(input("Digite la longitud maxima: "))
        controller.req5(cont,latitud_min,latitud_max,longitud_min,longitud_max)
    else:
        sys.exit(0)

sys.exit(0)
