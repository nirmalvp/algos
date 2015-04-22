#Given a Number N , write a function to calculate how many times the digit M appear in numbers in range 1-N. M is [1-9].
def countOccurenceOfDigitAtPosition(digitPosition,m):
	powerOfTen = 10 ** digitPosition
	nextPowerOfTen = 10 * powerOfTen
	digit = (num/powerOfTen) % 10
	numberToTheRight = num % powerOfTen
	roundDown = num - (num % nextPowerOfTen)
	roundUp = nextPowerOfTen + roundDown
	if digit < m :
		return roundDown/10
	if digit > m :
		return roundUp/10
	if digit == m :
		return roundDown/10 + (numberToTheRight+1)

num = input("Enter the number")
m = input("Enter the digit which is to be counted")
count = 0
for digitPosition,_ in enumerate(str(num)):
	count += countOccurenceOfDigitAtPosition(digitPosition,m)
print "Number of digit %s in %s = %s"%(m,num,count)