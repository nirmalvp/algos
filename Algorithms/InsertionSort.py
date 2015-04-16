userInput = raw_input("Enter list with commas")
userInput = userInput.replace(" ","")
arrayToSort = [int(i) for i in userInput.split(',')]

for currentElementIndex in range(1,len(arrayToSort)):
	temp=arrayToSort[currentElementIndex]
	previousElementIndex = currentElementIndex-1
	while (previousElementIndex >= 0 and arrayToSort[previousElementIndex] > temp ):
		arrayToSort[previousElementIndex+1] = arrayToSort[previousElementIndex]
		previousElementIndex = previousElementIndex - 1
	arrayToSort[previousElementIndex+1] = temp

print arrayToSort



