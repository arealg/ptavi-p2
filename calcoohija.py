#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calc


class CalculadoraHija(calcoo.Calculadora):

    def dividir(self, x, y):
        try:
            return x/y
        except:
            sys.exit('Division by zero is not allowed')

    def multiplicar(self, x, y):
        return x*y


def modo_operacion(modelo, numero1, numero2):
    solucion = modelo(numero1, numero2)
    print (solucion)


def operando_valido(operando, numero1, numero2):

    calculo = CalculadoraHija()
    libreria = {'suma': calculo.sumar, 'resta': calculo.restar,
                'multiplica': calculo.multiplicar, 'divide': calculo.dividir}
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
