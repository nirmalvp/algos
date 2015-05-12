#2) Given an array, find the longest continuous increasing subsequence.
def lis(array):
	lisLength=[1 for element in array]
	parentDict = dict()
	maxSequenceLength = 1
	for index,element in enumerate(array):
		for prevIndex in range(index):
			if array[prevIndex] < element and lisLength[prevIndex] + 1 > lisLength[index]:
				lisLength[index] = lisLength[prevIndex] + 1
				parentDict[index] = prevIndex
				if lisLength[index] > maxSequenceLength :
					maxSequenceLength = lisLength[index]
					maxSequenceIndex = index
	return maxSequenceIndex,parentDict
def main():
	array = map(int,raw_input("Enter list of elements : ").split())
	maxSequenceIndex,parentDict = lis(array)
	path =list()
	index = maxSequenceIndex
	while parentDict.get(index)!=None:
		path.append(array[index])
		index = parentDict.get(index)
	path.append(array[index])
	path.reverse()
	print path,
main()

