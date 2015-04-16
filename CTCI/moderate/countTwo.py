def findTwos(digitPosition):
	power10 = 10 ** digitPosition
	next10 = 10*power10
	right = num % power10

	digit = (num/power10) % 10
	roundDown = num - (num%next10)
	roundUp = roundDown + next10
	if(digit<2):
		return roundDown/10
	if(digit>2):
		return roundUp/10
	else :
		return roundDown/10 + (right+1)

count =0
num = input("Enter the number")
for digitPosition,_ in enumerate(str(num)):
	count+=findTwos(digitPosition)
print count




