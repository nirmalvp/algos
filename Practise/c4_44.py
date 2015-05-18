#44) Given an array with integer, write code to put all odd number before even number.

def oddBeforeEveningUsingSort(array):
	return sorted(array,key = lambda x : x % 2,reverse = True)

def oddBeforeEven(array):
	i = 0
	j = len(array)-1
	while True:
		while i<j and array[i] %2 != 0 : #iterate till even num found
			i+=1
		while j>i and array[j] % 2 == 0 : # iterate till even found
			j = j-1
		if i < j :
			array[i],array[j] = array[j], array[i]
		else:
			break
	return array

def main():
	array = map(int,raw_input("enter the array").split())
	print oddBeforeEven(array[:])
	print oddBeforeEveningUsingSort(array)
main()