num=1913
myArray=list()
while num:
	digit = num%10
	num /= 10
	myArray.append(digit)
print myArray
for digit in reversed(myArray):
	
