#76A) Given a collection of numbers, return all possible combinations
def findNcK(numbers,k):
	for index,number in enumerate(numbers):
		if k == 1 :
			yield (number,)
		else :
			for prevComb in findNcK(numbers[index+1:],k-1):
				yield (number,) + prevComb

def allPossibleCombinations(numbers):
	for k in range(1,len(numbers)+1):
		print list(findNcK(numbers,k))

def main():
	numbers = map(int,raw_input("Enter the numbers").split())
	allPossibleCombinations(numbers)
main()