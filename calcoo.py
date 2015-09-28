#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calc


class Calculadora:

    def sumar(self, x, y):
        return x+y

    def restar(self, x, y):
        return x-y


def modo_operacion(calc_operac, numero1, numero2):
    solucion = calc_operac(numero1, numero2)
    print (solucion)


def operando_valido(operacion, numero1, numero2):
    calculo = Calculadora()
    libreria = {'suma': calculo.sumar, 'resta': calculo.restar}

    try:
        modo_operacion(libreria[operacion], numero1, numero2)
    except:
        print ('Error: Non operation parameters')


if __name__ == '__main__':

    sum1 = sys.argv[1]
    sum2 = sys.argv[3]
    operacion = sys.argv[2]

    try:
        numero1 = calc.es_float(sum1)
        numero2 = calc.es_float(sum2)
        operando_valido(operacion, numero1, numero2)
    except ValueError:
        print ('Error: Non numerical parameters')
