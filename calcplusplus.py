#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import sys
from calcoo import Calculadora
from calcoohija import CalculadoraHija

with open(sys.argv[1], newline='') as csv_archivo:
	entrada = csv.reader(csv_archivo)
	for line in entrada:
		operador = line[0]
		operandos = line[1:]
		result = int(operandos[1])
		for op in operandos[2:]:
			#no se porque no me lee el primer operando
			#las operaciones se hacen bien pero falta el primero
			#acordarse de mirar calcoohija en division 0 none
			if operador == 'suma':
				result = Calculadora(result, int(op)).plus()
			elif operador == 'resta':
				result = Calculadora(result, int(op)).minus()
			elif operador == 'multiplica':
				result = CalculadoraHija(result, int(op)).multiply()
			elif operador == 'divide':
				result = CalculadoraHija(result, int(op)).division()

		print(result)

