#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoo import Calculadora
from calcoohija import CalculadoraHija

infile= open(sys.argv[1], 'r')


for line in infile:
	operador = line.split(',')[0]
	operandos = line.split(',')[1:]
	result = int(operandos[0])
	for op in operandos[1:]:
		if operador == 'suma':
			result = Calculadora(result, int(op)).plus()
		elif operador == 'resta':
			result = Calculadora(result, int(op)).minus()
		elif operador == 'multiplica':
			result = CalculadoraHija(result, int(op)).multiply()
		elif operador == 'divide':
			result = CalculadoraHija(result, int(op)).division()

	print(result)	
