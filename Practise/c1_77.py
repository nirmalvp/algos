#77) The gray code is a binary numeral system where two successive values differ in only one bit.   [LeetCode]    
#        Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.        
#        For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:  00 - 0  01 - 1  11 - 3  10 - 2 
def printGreyCodeRecursive(bits):
	if bits == 1:
		return [0,1]
	prevGreyCode = printGreyCode(bits-1)
	greyCode = list(prevGreyCode)
	# When bits =2,greyCode = [0,1] now append 1 to left of each element in greyCode reversed to get [0,1,11,10]. 
	#using shifted to attain proper bit position of 1
	shifted = (1<<(bits-1))
	for number in reversed(prevGreyCode):
		greyCode.append( shifted | number )
	return greyCode

def printGreyCodeIterative(bits):
	greyCode = [0,1]
	if bits == 1:
		return greyCode
	for bitPosition in range(1,bits):
		shifted = (1<<bitPosition)
		for number in reversed(greyCode[:]):
			greyCode.append( shifted | number )
	return greyCode

def main():
	bits = input("Enter Number of bits")
	print printGreyCodeRecursive(bits)
	print printGreyCodeIterative(bits)

main()



