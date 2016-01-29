#!/usr/bin/env python
import sys
import re

numeros = 0
temp = 0
nuevalinea = ""

try:
	for linea in sys.stdin:
		nuevalinea = ""
		for char in linea:
			if char != ":" and char != "\"" and char !="\\/" and char !="#":
				temp = ord(char) + 3
				char = chr(temp)
				nuevalinea = nuevalinea + char
		print nuevalinea
except IOError:
    # stdout is closed, no point in continuing
    # Attempt to close them explicitly to prevent cleanup problems:
    try:
        sys.stdout.close()
    except IOError:
        pass
    try:
        sys.stderr.close()
    except IOError:
        pass