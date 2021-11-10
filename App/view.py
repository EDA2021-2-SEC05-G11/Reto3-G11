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
    print("3- Contar los avistamientos en un rango de horas.")
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

    elif int(inputs[0]) == 3:
        lim_inicial = "2000-01-01, " + str(input("Ingrese el limite inicial de la hora: \n"))
        lim_final = "2000-01-01, " + str(input("Ingrese el limite final de la hora: \n"))
        controller.req3(cont, lim_inicial, lim_final)

    else:
        sys.exit(0)

sys.exit(0)
