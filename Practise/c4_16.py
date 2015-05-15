#16) Write code to reverse a array of int
def reverseArray(array):
	forwardPointer = 0
	backwardPointer = len(array)-1
	while forwardPointer<= backwardPointer :
		array[forwardPointer], array[backwardPointer] = array[backwardPointer], array[forwardPointer]
		forwardPointer+= 1
		backwardPointer -= 1
	return array

def main():
	print reverseArray(map(int,raw_input("ENter array to reverse").split()))
main()