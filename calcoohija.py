#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoo import Calculadora


class CalculadoraHija:

    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def multiply(self):
        return self.op1 * self.op2

    def division(self):
        try:
            return self.op1 / self.op2
        except ZeroDivisionError:
            return 'Division by zero is not allowed'


if __name__ == "__main__":
    try:
        operacion = CalculadoraHija(int(sys.argv[1]), int(sys.argv[3]))
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "multiplica":
        result = operacion.multiply()
    elif sys.argv[2] == "divide":
        result = operacion.division()
    elif sys.argv[2] == "suma":
        result = operacion.plus()
    elif sys.argv[2] == "resta":
        result = operacion.minus()
    print(result)
