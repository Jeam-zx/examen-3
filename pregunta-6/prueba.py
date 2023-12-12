"""
A continuacion se presenta un subconjunto del
interprete de prolog
"""

import sys
import string
import re

"""
Definimos la Memoria
"""
hechos = {}
reglas = {}

"""
Recibe del usuario los argumentos y los distribuye
sobre las funciones pertinentes
"""


def ejecutar(accion, argumentos):
    if (accion == "DEF"):
        definir(argumentos)
    elif (accion == "ASK"):
        consultar(argumentos)
    elif (accion == "SALIR"):
        sys.exit()
    else:
        print("Error en el Formato de Entrada")


"""
Maneja la instruccion DEF
Si lo que recibe es un hecho lo registra como tal
y si lo que recibe es una regla
ejecuta la funcion pertinente
"""


def definir(argumentos):
    arg = argumentos.split(') ')
    for i in range(len(arg) - 1): arg[i] = arg[i] + ")"
    if len(arg) == 1:
        print(definir_hecho(arg[0], hechos))
    else:
        print(definir_regla(arg, reglas))


"""
Se registran los hechos en la memoria
"""


def definir_hecho(argumento, hechos):
    if not any(c in string.ascii_uppercase for c in argumento):
        nombre = argumento.split('(')[0]
        args = obtenerContenido(argumento)
        if nombre in hechos:
            hechos[nombre].append(args)
        else:
            hechos[nombre] = [args]
        return "Se definió el hecho '" + argumento + "'"
    else:
        return "Los Hechos no contienen Variables"


"""
Obtener lista contenido de argumento
"""


def obtenerContenido(argumento):
    if '(' in argumento:
        i = argumento.find('(')
        j = argumento.rfind(')')
        contenido = argumento[i + 1:j].split(',')
        for k in range(len(contenido)):
            contenido[k] = contenido[k].strip()
        return contenido
    else:
        return []


"""
Se registran las reglas en la memoria
"""


def definir_regla(argumentos, reglas):
    nombre = argumentos[0]
    args = argumentos[1:]
    if any(c in string.ascii_uppercase for c in " ".join(args)):
        if not nombre in reglas:
            reglas[nombre] = [args]
        else:
            reglas[nombre].append(args)
        return "Se definió la regla " + " ".join(argumentos)
    else:
        return "El valor introducido no corresponde a una regla"


"""
Maneja la instruccion de consulta
"""


def consultar(argumentos):
    arg = argumentos.split('(')
    nombre = arg[0]
    for i in range(len(arg) - 1): arg[i] = arg[i] + ")"
    if len(arg) == 1:
        print(ejecutar_consulta(nombre, arg[1]))
    else:
        print("No cumple el formato de consulta")


"""
Se ejecuta la consulta
"""


def ejecutar_consulta(nombre, argumentos):
    args = argumentos.split(',')
    tupla = args.copy()
    for i in range(len(args)):
        args[i] = args[i].strip()
        if any(c in string.ascii_upercase for c in args[i]):
            tupla[i] = False
        else:
            tupla[i] = args[i]

    # if( nombre in reglas ):
    #     lista = reglas[nombre]
    #     for i in lista:
    #         n = len(i)
    #         for j in range(n):
    #             if tupla[j] != False and tupla[j] == :
    #                 tupla[j] =


"""
Ejecuta un bucle recibiendo solicitudes
del usuario
"""


def main():
    entrada = input(">> ")
    entrada = entrada.split(" ")
    try:
        accion = entrada[0]
        argumentos = ""
        if accion != "SALIR":
            argumentos = " ".join(entrada[1:])
        ejecutar(accion, argumentos)
    except IndexError:
        print("Error en el formato de entrada")
    main()


"""
Si se llama desde este archivo
se ejecuta la funcion main()
"""
if __name__ == "__main__":
    main()