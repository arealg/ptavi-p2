#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calc


class Calculadora:

    def sumar(self, x, y):
        return x+y

    def restar(self, x, y):
        return x-y


def mod_operacion(calc_operac, numero1, numero2):
    solucion = calc_operac(numero1, numero2)
    print (solucion)


def operacion_valida(operacion, numero1, numero2):
    calculo = Calculadora()
    op_val = {'suma': calculo.sumar, 'resta': calculo.restar}

    try:
        mod_operacion(op_val[operacion], numero1, numero2)
    except:
        print ('Error: Non operation parameters')


if __name__ == '__main__':

    sum1 = sys.argv[1]
    sum2 = sys.argv[3]
    operacion = sys.argv[2]

    try:
        numero1 = calc.find_float(sum1)
        numero2 = calc.find_float(sum2)
        operacion_valida(calculo, operacion, numero1, numero2, op_val)
    except ValueError:
        print ('Error: Non numerical parameters')
