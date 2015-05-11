#78) Roman to integer and integer to Roman. 
#TODO: Need to Fix ROman to integer
def isPowerOfTen(digit):
	return digit in [1,10,100,100]

def romanToInteger(romanNumber,numerals):
	index = 0
	number=0
	while index < len(romanNumber) :
		char= romanNumber[index]
		if char not in numerals:
			print "Invalid ROman NUmber"
			return
		digit = numerals.get(char)
		if index != len(romanNumber)-1:
			nextChar = romanNumber[index+1]
			if nextChar not in numerals:
				print "invalid Roman NUmber"
				return
			nextDigit = numerals.get(nextChar)
			if isPowerOfTen(digit) and nextDigit digit:
				number += nextDigit - digit
				index +=2
				continue
		number += digit
		index +=1
	return number

def integerToRoman(number,literals):
	powerOfTen = 1
	romanRepr = ""
	while number/powerOfTen >= 10:
		powerOfTen = powerOfTen * 10
	while number > 0:
		leftMostDigit = number / powerOfTen
		if leftMostDigit == 4 or leftMostDigit == 9 :
			romanRepr += literals.get(powerOfTen)
			romanRepr += literals.get((leftMostDigit+1)*powerOfTen)
			number = number % powerOfTen
			powerOfTen = powerOfTen / 10
		else:
			for value in sorted(literals,reverse=True):
				if value <= number:
					romanRepr += literals.get(value) * (number/value)
					break			
			number = number % value
			if number/powerOfTen == 0 :
				powerOfTen = powerOfTen/10
	return romanRepr

def main():
	numerals={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
	literals = {value:key for key,value in numerals.iteritems()}
	print romanToInteger(raw_input("Enter the roman number"),numerals)
	for i in range (1,1100):
		print i, integerToRoman(i,literals)

main()
