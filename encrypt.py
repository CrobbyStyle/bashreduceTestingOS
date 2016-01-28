#!/usr/bin/env python
import sys
import re

numeros = 0
temp = 0
frase = ""

for linea in sys.stdin:
	
	for char in linea:
		if char != ":" and char != "\"":
			if char.isdigit():
				numeros = numeros + int(char)
			else:
				temp = ord(char) + 3
				char = chr(temp)
				frase = frase + char

	print frase

