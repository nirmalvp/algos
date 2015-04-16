#14) Write a method to get the greatest common divisor(GCD) of two given integer.

def gcd(x,y):
	while y != 0 :
		x,y = y, x%y
	return x
x = input("Num 1 : ")
y = input("Num 2 : ")

print gcd(x,y)

