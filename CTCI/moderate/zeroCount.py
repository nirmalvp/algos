#Compute trailing zeroes in n factorial
num = input("enter n for which factorial has to be calculated")
twoCount=0
fiveCount=0
for num in xrange(num,0,-1):
	while(num!=0 and (num%2==0 or num%5==0)):
		if(num%2==0):
			twoCount+=1
			num/=2
		if(num%5==0):
			fiveCount+=1
			num/=5
print "Number of trailing zeros in factorial = ",min(twoCount,fiveCount)
