# 25) You are given an unsorted array of integers that contain duplicate numbers.
# Only one number is duplicated odd number of duplications, other numbers are repeated even number of duplications
# Find this number

def findDuplicate(array):
	duplicate = 0
	for element in array:
		duplicate = duplicate ^ element
	return duplicate

def main():
	array = map(int,raw_input("Enter the element of array").split())
	print findDuplicate(array)
main()