#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoo import Calculadora

class CalculadoraHija:
	def multiply(op1, op2):
		"Function to multiply the operants"
		return op1 * op2

	def division(op1, op2):
		"Function to division the operants"
		return op1 / op2

if __name__ == "__main__":
	try:
		operando1 = int(sys.argv[1])
		operando2 = int(sys.argv[3])
	except ValueError:
		sys.exit("Error: Non numerical parameters")

	if sys.argv[2] == "multiplica":
		result = CalculadoraHija.multiply(operando1, operando2)
	elif sys.argv[2] == "divide":
		if sys.argv[3] == "0":
			result = "Division by zero is not allowed"
			
		else:
			result = CalculadoraHija.division(operando1, operando2)
	#Quiero saber si esto puedo implementar directamente la calculadora sin tener que repetir codigo
	elif sys.argv[2] == "suma":
		result = Calculadora.plus(operando1, operando2)
	elif sys.argv[2] == "resta":
		result = Calculadora.minus(operando1, operando2)
	print(result)
	

