#Given an int array, combine all the integer to a int, such as {23, 125} -> 12523.
# Write code to get the smallest combined number.


def smallestCombinedNumber(array):
	lexicographSortedArray = sorted(array,key = str)
	return "".join(str(num) for num in lexicographSortedArray)

def main():
	array = map(int,raw_input("Enter the elements of the array").split())
	print smallestCombinedNumber(array)
main()