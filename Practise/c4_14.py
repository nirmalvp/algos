#Given a set S, find all the maximal subsets whose sum <= k.
def subsetSumLessThanK(k,inputSet):
	for index,element in enumerate(inputSet):
		if element <= k :
			current = (element,)
			yield current
			for prevSet in subsetSumLessThanK(k-element,inputSet[index+1:]):
				yield prevSet
				yield current + prevSet
def main():
	inputSet = map(int,raw_input("Enter the element of the set").split())
	k = input("enter the value of k")
	for subsets in set(subsetSumLessThanK(k,inputSet)):
		print subsets,
main()