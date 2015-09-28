#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcplus
import calcoohija

if __name__ == '__main__':

    fichero = sys.argv[1]
    with open(fichero) as fichero1:
        lineas = csv.reader(fichero1)
        for linea in lineas:
            calcplus.operando_valido(linea[0], linea)
