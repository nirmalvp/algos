num = int(raw_input("Number :"))
temp = num
count = 0
nextBig = None
prevSmall = None
while (temp !=0):
 	if(num & (1<<count) != 0):
 		oneRemoved = num & ~(1<<count)
 		nextBig = oneRemoved | (1<<(count+1))
 		if(count != 0):
 			prevSmall = oneRemoved | (1<<(count -1))
 		break
 	temp = temp >> 1
 	count+=1

print "Next big = ",nextBig, "previous small = ", prevSmall



