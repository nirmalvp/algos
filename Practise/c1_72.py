def checkPalindrome(num):
	powerOfTen  = 1
	while num / powerOfTen >= 10 :
		powerOfTen = powerOfTen * 10  
	while num > 0 :
		left = num / powerOfTen
		right = num % 10
		if left != right :
			return False
		num = (num % powerOfTen)/10
		powerOfTen = powerOfTen / 100
	return True

def main():
	num = input("Enter the number")
	if checkPalindrome(num) :
		print "%s is a palindrome "%num
	else :
		print "%s is not a palindrome"%num

main()