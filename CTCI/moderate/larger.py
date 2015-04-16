from math import sqrt
num1 = input("First num :")
num2 = input("Second num :")
try:
	sqrt(num1-num2)
	print num1,">=",num2
except ValueError:
	print num2,">=",num1


