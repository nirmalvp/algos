#Given a file of 4 billion 32-bit integers, how to find one that appears at least twice?

#Solution using pigeon hole theory
countofEachPrefix = [0] * (2**16) #Count of numbers appearing with each prefix 
for num in fourBillionNumbers :
	prefix = num >> 16 # 16 left most bits
	countofEachPrefix[prefix]+=1
	if countofEachPrefix[prefix] > (1<<16)  : # Since 4 billion > 2^32, the maximum number of distinct number that can be made with 
											  #32 bits, atleast one prefix would have more than 2**16 count(max distinct number that
											  # can be made with the remaining 16 bits combined with prefix). 
											   #Check with 2 bit numbers and file of 5 numbers to verify.
		break

countofEachPrefix = [] #Clearing memory
countofEachSuffix =[0] * (2**16) 
prefix = prefix << 16 						# Moving prefix to last 16 bits
for num in fourBillionNumbers:
	suffix = num ^ prefix
	if(suffix < (1<<16) ) : # if first 16 bits of num are same as prefix, first 16 bits will be 0,so the suffix will be less than
							# 2**16. If the if condition passes, it means the num,has the same first 16 bits as prefix
		if countofEachSuffix[suffix] == 1 : # Already found the number
			print num, " is duplicated"
		else:
			countofEachSuffix[suffix] += 1

#No Duplicate found

	