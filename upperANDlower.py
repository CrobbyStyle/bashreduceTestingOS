#!/usr/bin/env python
import sys
import re

for row in sys.stdin:

	newstring = ""

	for char in row:

    		if char.isupper():
        		newstring += char.lower()
    		elif char.islower():
        		newstring += char.upper()

	print newstring
