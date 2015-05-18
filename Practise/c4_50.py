# 50) Given an array contains positive and negitive numbers, write code to re-arrange the array to make negitive number placed before positive number
#and the relative position of positive numbers and negitive numbers are not changed.
#        The best code should be: time O(N) and space O(1)

def reArrangePosAndNeg(array):
	i = 0
	j = len(array) - 1
	while  True:
		while i<j and array[i]<=0: # Iterate till a positive num encountered
			i+=1
		while j>i and array[j] >= 0 : #Iterate till negitive num encountered
			j = j-1
		if i<j :
			array[i],array[j] = array[j],array[i]
		else:
			break
	return array
def main():
	array = map(int,raw_input("Enter the array").split())
	print reArrangePosAndNeg(array[:])
main()