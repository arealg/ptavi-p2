#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora

import sys


def sumar(x, y):
    return x+y


def restar(x, y):
    return x-y


def find_float(sumando):
    if '.' in sumando:
        return float(sumando)
    else:
        return int(sumando)


def operacion_valida(operacion, numero1, numero2):
    if operacion == 'suma':
        print(sumar(numero1, numero2))
    elif operacion == 'resta':
        print(restar(numero1, numero2))
    else:
        print('Non operation parameters')


if __name__ == '__main__':

    sum1 = sys.argv[1]
    sum2 = sys.argv[3]
    operacion = sys.argv[2]

    try:
        numero1 = find_float(sum1)
        numero2 = find_float(sum2)
        operacion_valida(operacion, numero1, numero2)
    except ValueError:
        print('Error: Non numerical parameters')
