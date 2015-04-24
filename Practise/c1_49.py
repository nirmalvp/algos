#http://stackoverflow.com/questions/29822126/build-smallest-number-larger-than-k-using-only-allowed-digits
#Given an int array, numbers between 0-9, such as [0,1,3,8], write code to find the closest number built by these numbers larger then K.  [Google]
        #Such as [0,1] and K = 21, should return 100.
def isPossibleToMakeKWithoutTheLastDigit(numWithLastDigitRemoved,allowedDigits):
	for digit in numWithLastDigitRemoved:
		if digit not in allowedDigits:
			return False
	return True

def findSmallestNumberGreaterThanDigit(lastDigit,allowedDigits):
	for allowedDigit in sorted(allowedDigits):
		if allowedDigit > lastDigit:
			return allowedDigit
	return -1

def convertListToNumber(listOfNumber):
	return reduce(lambda x,y: x*10 + y ,listOfNumber)

def findNextLargest(k,allowedDigits):
	lastDigit = k[-1]
	kWithLasDigitRemoved = k [:-1]
	smallestNumberGreaterThanLastDigit = findSmallestNumberGreaterThanDigit(lastDigit,allowedDigits)
	if len(k)==1 : #Base Case
		if smallestNumberGreaterThanLastDigit != -1: 
			return [smallestNumberGreaterThanLastDigit]
		else : #There are no single Digit greater than current k in allowedDigits. So, go for two digits
			minimumAllowedDigit = min(allowedDigits) 
			if minimumAllowedDigit == 0: #0 Cant be in the ten's position,So find second minimum
				return [sorted(allowedDigits)[1],0]
			else :
				return [minimumAllowedDigit,minimumAllowedDigit]
	if isPossibleToMakeKWithoutTheLastDigit(kWithLasDigitRemoved,allowedDigits) and smallestNumberGreaterThanLastDigit != -1 :
		return kWithLasDigitRemoved + [smallestNumberGreaterThanLastDigit]
	return findNextLargest(kWithLasDigitRemoved,allowedDigits) + [min(allowedDigits)]


def main():
	k = map(int,raw_input("enter number")) #Saving num as an array of digits
	allowedDigits = set(map(int,raw_input("enter allowed Digits")))
	print convertListToNumber(findNextLargest(k,allowedDigits))

main()