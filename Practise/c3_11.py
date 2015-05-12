#11) You have two numbers represented by a linked list, where each node contains a single digit, The digit are stored in reverse order
#        617 == 7->1->6
#        Write a function to adds the two numbers and returns the sum as a linked list.
from c3_linkedlist import LinkedList
def addNumbers(num1,num2) :
	sumList = LinkedList()
	firstNumPointer = num1.first
	secondNumPointer = num2.first
	sumCarry = 0
	while firstNumPointer and secondNumPointer :
		sumofdigits = ( firstNumPointer.data + secondNumPointer.data + sumCarry ) 
		sumDigit = sumofdigits % 10
		sumCarry = sumofdigits / 10
		sumList.insert(sumDigit)
		firstNumPointer = firstNumPointer.next
		secondNumPointer = secondNumPointer.next
	
	while firstNumPointer :
		sumofdigits = ( firstNumPointer.data + sumCarry ) 
		sumDigit = sumofdigits % 10
		sumCarry = sumofdigits / 10
		sumList.insert(sumDigit)
		firstNumPointer = firstNumPointer.next

	while secondNumPointer :
		sumofdigits = ( secondNumPointer.data + sumCarry ) 
		sumDigit = sumofdigits % 10
		sumCarry = sumofdigits / 10
		sumList.insert(sumDigit)
		secondNumPointer = secondNumPointer.next

	if sumCarry != 0 :
		sumList.insert(sumCarry)
	return sumList

def main():
	num1 = LinkedList()
	num2 = LinkedList()
	for digit in reversed(raw_input("Enter the First number : ")) :
		num1.insert(int(digit))
	for digit in reversed(raw_input("Enter the Second number : ")) :
		num2.insert(int(digit))
	sumList = addNumbers(num1,num2)
	print "Sum = (In reversed Form) ", 
	sumList.show()

main()
