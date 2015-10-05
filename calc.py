#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora

import sys


def sumar(x, y):
    return x+y


def restar(x, y):
    return x-y


def es_float(sumando):
    try:
        if '.' in sumando:
            return float(sumando)
        else:
            return int(sumando)
    except ValueError:
        sys.exit('Error: Non numerical parameters')


def operando_valido(operacion, numero1, numero2):
    libreria = {'suma': sumar(numero1, numero2),
                'resta': restar(numero1, numero2)}

    try:
        print (libreria[operacion])
    except KeyError:
        sys.exit('Error: Non operation parameter')

if __name__ == '__main__':

    sum1 = sys.argv[1]
    sum2 = sys.argv[3]
    operacion = sys.argv[2]

    numero1 = es_float(sum1)
    numero2 = es_float(sum2)
    operando_valido(operacion, numero1, numero2)
