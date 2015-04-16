 # * Problem: Remove all the number containing the specified digit from the integer series
 # * Key Idea: 
 # * 	  1. When we need remove a particular number from a integer series, it could be consider
 # * 		 to format the integer to base-9 system.
 # * 	  2. During the format, replace particular number to allowed number by mapping.

def removeDigit(rangeofNum,excludedDigit):
	base = 9 # The base will be 9 since the excluded Digit is no more considered
	for num in rangeofNum:
		recreatedNumber = 0
		tenPosition = 0
		temp = num
		while (num>0):
			digit = num%base
			num = num / base
			if digit >= excludedDigit:
				digit += 1
			recreatedNumber = recreatedNumber + (digit * 10**tenPosition)
			tenPosition += 1
		print temp, " ", recreatedNumber
		

rangeofNum = input("Enter higher limit of the integer series required :")
excludedDigit = input("Input digit to be excluded from series : ")
removeDigit(range(rangeofNum),excludedDigit)

