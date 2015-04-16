# 15) Write a method to transfrom a string to int.
def convertToInt(numberString):
	number = 0
	negativeNumber = False
	if(numberString[0] == "-"):
		negativeNumber = True
		numberString=numberString[1:]
	for digitString in numberString:
		if( 48 <= ord(digitString) <=57):
			digitNum = ord(digitString) - 48
			number = number * 10 + digitNum
		else:
			raise ValueError("Not a number")
	if negativeNumber:
		number = -number
	return number
numberString = raw_input("Enter a number")
print convertToInt(numberString)

