# 11) Randomly shuffle an array.
from random import randint 
def randomShuffleArray(array,lastIndex):
	for index,_ in enumerate(array):
		randomIndex = randint(index,lastIndex) #randint is inclusive of range
		array[index],array[randomIndex] = array[randomIndex], array[index]
def main():
	array = map(int,raw_input("Enter the element of array to be shuffled").split())
	randomShuffleArray(array,len(array)-1)
	print array
main()

