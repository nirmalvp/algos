#Having N, find there exist how many continuous int sequence which sum is N. 
        #Such as Given 15, 1+2+3+4+5 = 4+5+6 = 7+8 = 15, so output should be 3.

num = input("enter the number : ")
continousSum = 0
remove =1 
count = 0 
for factor in range( (num/2 + 1) + 1 ): # We don't have to check more than the half of the number 
	continousSum += factor 
	while continousSum > num : #Remove first n consecutive numbers from the sum till sum becomes less than num. No point adding 
								# a new number if the sum already exceeds the num.  
		continousSum = continousSum - remove
		remove += 1
	if continousSum == num : 
		count +=1
print "No: of continuous int sequence = ",count
