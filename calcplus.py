#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoo import Calculadora
from calcoohija import CalculadoraHija

infile= open(sys.argv[1], 'r')

operadores = []
operandos = []

for line in infile:
	operadores.insert(0,line[:line.find(",")])
	operandos.insert(0,line[:line.find(' ')].split(',')[1:])
print(operadores)
print('xxxxxxxxxxxxxxxxxxxxxxxxxx')
print(operandos)

if __name__ == "__main__":
	try:
		suma = operadores[0]
		resta = operadores[1]
		multiplica = operadores[2]
		divide = operadores[3]
	except ValueError:
		sys.exit("Error: Non numerical parameters")

	

	
	

