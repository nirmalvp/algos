#58) Given a int N, write code to find the N which is the closet number is power of 2.
def findPowerOfTwoGreaterThanNum(num):
	powerOfTwo = 1
	while powerOfTwo < num :
		powerOfTwo = powerOfTwo << 1
	return powerOfTwo
def main():
	num = input("Enter the num")
	powerOfTwoGreaterThanNum = findPowerOfTwoGreaterThanNum(num)
	powerOfTwoLesserThanNum = powerOfTwoGreaterThanNum >> 1
	print min(powerOfTwoLesserThanNum,powerOfTwoGreaterThanNum, key = lambda x : abs(x-num) )
main()