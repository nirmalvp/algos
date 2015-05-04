#Given a integer, write code to find a combination of continuous integer which sum is the given integer
def findConsecutiveIntegers(number):
	consecutiveIntegersList = list()
	sumOfNumbers = 0
	for consecutiveNumber in range ( 1, number/2 +2 ):
		consecutiveIntegersList.append(consecutiveNumber)
		sumOfNumbers += consecutiveNumber
		while  sumOfNumbers > number:
			toRemoveNumber = consecutiveIntegersList.pop(0)
			sumOfNumbers = sumOfNumbers - toRemoveNumber
		if sumOfNumbers == number:
			print consecutiveIntegersList
			print
			
def main():
	number = input("enter the number")
	findConsecutiveIntegers(number)
main()

