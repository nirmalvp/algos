def countOneinBinary(num):
	count =0
	i=0
	while num > 0:
		if num & 1 > 0:
			count +=1
		num = num >> 1
	return count
num=input("Enter nUmber : ")
print countOneinBinary(num)