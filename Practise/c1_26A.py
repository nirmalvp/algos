num1 = input("Number 1 :")
num2 = input("Number 2 :")

def countOneinBinary(num):
	count =0
	while num > 0:
		count += num & 1
		num = num >> 1
	return count

def numberOfDifferentBits(num1,num2):
	diff = num1 ^ num2
	return countOneinBinary(diff)

print numberOfDifferentBits(num1,num2)