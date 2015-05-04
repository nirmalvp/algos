#A circus is designing a tower routine consisting of people standing atop one anothers shoulders
#For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her.
#Given the heights and weights of each person in the circus,
#write a method to compute the largest possible number of people in such a tower
#EXAMPLE:
#Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
#Output: The longest tower is length 6 and includes from top to bottom: (56, 90) (60,95) (65,100) (68,110) (70,150) (75,190
def getInput():
    while True:
    	heights = map(int,raw_input("Enter the heights of people : ").split())
    	weights = map(int,raw_input("Enter the weights of people : ").split())
    	if len(heights) == len(weights):
    		return heights,weights
    	else:
    		print "Wrong Input"

def longestIncreasingSubsequence(people):
	parent = {}
	weights = [weight for height,weight in people]
	listLength = [1] * len(weights)
	maxSequenceLength = 1
	for index, weight in enumerate(weights):
		for previousIndex in range(index):
			if weights[previousIndex] < weight and listLength[previousIndex] + 1 > listLength[index] :
				listLength[index] = listLength[previousIndex] + 1
				parent[index] = previousIndex
				if listLength[index] > maxSequenceLength :
					bestEnd = index
					maxSequenceLength = listLength[index]
	return maxSequenceLength, parent, bestEnd

def printResult(maxSequenceLength, parent, bestEnd,people):
	print "Max number of people = ",maxSequenceLength
	while parent.get(bestEnd) !=None :
		print people[bestEnd],
		bestEnd = parent.get(bestEnd)
	print people[bestEnd]

def main():
    heights, weights = getInput()
    people = zip(heights,weights)
    people.sort() # People are now sorted according to increasing order of heights
    maxSequenceLength, parent, bestEnd = longestIncreasingSubsequence(people) # Since the list is now ordered by height, we just have to find LIS of the weights
    #to get the max number of people who can form the formation
    printResult(maxSequenceLength, parent, bestEnd, people)
main()


