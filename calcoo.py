#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calc


class Calculadora:
    def __init__(self):
        self.libreria = {'suma': self.sumar, 'resta': self.restar}


    def sumar(self, x, y):
        return x+y

    def restar(self, x, y):
        return x-y


def modo_operacion(tipo_operacion, numero1, numero2):
    solucion = tipo_operacion(numero1, numero2)
    print (solucion)


def operando_valido(operacion, numero1, numero2):
    calculo = Calculadora()

    try:
        modo_operacion(calculo.libreria[operacion], numero1, numero2)
    except KeyError:
        sys.exit('Error: Non operation parameter')


if __name__ == '__main__':

    sum1 = sys.argv[1]
    sum2 = sys.argv[3]
    operacion = sys.argv[2]

    numero1 = calc.es_float(sum1)
    numero2 = calc.es_float(sum2)
    operando_valido(operacion, numero1, numero2)
