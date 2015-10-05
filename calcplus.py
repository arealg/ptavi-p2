#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija


def modo_operacion(lista2, modelo):
    primero = int(lista2[1])
    for i in lista2[2:]:
        primero = modelo(primero, int(i))
    print(primero)


def operando_valido(operador, lista2):

    calcular = calcoohija.CalculadoraHija()
    libreria = {'suma': calcular.sumar, 'resta': calcular.restar,
                'multiplica': calcular.multiplicar, 'divide': calcular.dividir}

    try:
        modo_operacion(lista2, libreria[operador])
    except KeyError:
        print('Non operation parameter')


if __name__ == '__main__':

    fichero = sys.argv[1]
    fichero2 = open(fichero, 'r')
    texto = fichero2.read()
    fichero2.close
    lista = texto.split()

    for i in lista:
        operacion = str(i)
        lista2 = operacion.split(',')
        operador = lista2[0]
        operando_valido(operador, lista2)
