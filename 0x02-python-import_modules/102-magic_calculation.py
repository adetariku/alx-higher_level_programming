#!/usr/bin/python3
def magic_calculation(a, b):
	from calculator_1 import add, sub
	if b > a: 
		c = add(a,b)
		for i in range(4, 6):
			c = add(c,i)
		return c
	else:
		return (sub(a,b))
