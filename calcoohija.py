#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calc


class CalculadoraHija(calcoo.Calculadora):

    def __init__(self):
        super().__init__()
        self.libreria['divide'] = self.dividir
        self.libreria['multiplica'] = self.multiplicar

    def multiplicar(self, x, y):
        return x * y

    def dividir(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            sys.exit('Division by zero is not allowed')


def operando_valido(operando, numero1, numero2):
    calculo = CalculadoraHija()

    try:
        calcoo.modo_operacion(calculo.libreria[operacion], numero1, numero2)
    except KeyError:
        sys.exit('Error: Non operation parameter')


if __name__ == '__main__':

    sum1 = sys.argv[1]
    sum2 = sys.argv[3]
    operacion = sys.argv[2]

    numero1 = calc.es_float(sum1)
    numero2 = calc.es_float(sum2)
    operando_valido(operacion, numero1, numero2)
