#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import sys

with open(sys.argv[1], newline='') as csv_archivo:
	entrada = csv.reader(csv_archivo)
	for line in entrada:
		print(line)
