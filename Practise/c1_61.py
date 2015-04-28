#61) Given a integer N, find the minimal M to make N * M contains only 0 and 1.
        #such as: N = 2, M = 5, N * M = 10.

def findNextNumber(n):
	powerofTen = 1
	numbersMadeOfZeroAndOne = [1]
	checkedNumbers = [0] # Hack to get powerofTen+0 as a member of the list using map 
	count = 0
	while True:
		print numbersMadeOfZeroAndOne
		for number in numbersMadeOfZeroAndOne:
			count +=1
			if number % n == 0:
				return number / n
		checkedNumbers.extend(numbersMadeOfZeroAndOne)
		powerofTen = powerofTen * 10
		numbersMadeOfZeroAndOne = map(lambda number : powerofTen + number, checkedNumbers)

print findNextNumber(input("Enter the number"))

