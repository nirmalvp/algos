#70) Write a function that adds two numbers. You should not use + or any arithmetic operators.
def findSum(number1,number2):
	digitPosition  = 0
	c = 0
	sumOfNumber = 0
	while number1!=0 or number2!=0 :
		a = number1 & 1
		b = number2 & 1
		sumOfDigits = a ^ b ^ c
		c = (a&b) | (a&c) | (b&c)
		number1 = number1 >> 1
		number2 = number2 >> 1
		if sumOfDigits == 1 :
			sumOfNumber = (1 << digitPosition) | sumOfNumber 
		digitPosition +=1
	return sumOfNumber
		


def main():
	number1 = input("First number : ")
	number2 = input("Second number : ")
	print findSum(number1,number2)
main()
