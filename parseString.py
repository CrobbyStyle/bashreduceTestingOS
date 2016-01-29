#!/usr/bin/env python
import sys
import re

'''Credit: http://stackoverflow.com/questions/16544249/best-way-to-find-strings-between-two-points'''

suma = 0
frase = ""

for line in sys.stdin:

	suma = 0
	frase = ""
	
	commacount = 0

	for i in line:
	    if i == "\"" and commacount != 1:
	        commacount = 1
	    elif i == "\"" and commacount == 1:
	        commacount = 0
	        frase = frase + " "
	    if i != "\"" and commacount == 1:
	        if i.isdigit():
	        	suma = suma + int(i)
        	else:
        		frase = frase + i
	print suma

	frase = re.sub(r'[^a-zA-Z ]+', '', frase)

	print frase
			
	
