#31) Given two integer N and M, please find all the combination of numbers within[1,N] which sum is M.

def combinationToSum(startElement,lastElement,sumRequired):
	for element in range(startElement,lastElement+1):
		if element > sumRequired:
			return
		currentElement = (element,)
		if element == sumRequired :
			yield currentElement
		if element < sumRequired :
			for prevComb in combinationToSum(element,lastElement,sumRequired - element):
				yield currentElement + prevComb
def main():
	n,m = map(int,raw_input("Enter N in [1..N] and the sum sum Required").split())
	print list(combinationToSum(1,n,m))
main()
