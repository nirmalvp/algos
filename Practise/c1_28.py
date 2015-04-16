#28) Get the amount of ending zeros of N! without calculating N!

def trailingZero(factNum):
	countTwo = 0
	countFive = 0
	for num in range(factNum+1):
		while num!=0 and (num%2==0 or num%5==0) :
			if num%2 == 0:
				num = num /2
				countTwo += 1
			elif num%5 == 0 :
				num = num / 5
				countFive+=1
	return min(countTwo,countFive)

print trailingZero(input("Enter the number :"))