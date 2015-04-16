# Given a number, find the next largest number that can be created with a dfferent arrangement of the same set of digits

userInput= int(raw_input())
num = [int(i) for i in str(userInput)]
small = -1
for i in reversed( range(len(num))):
	if(num[i-1] < num[i]):
		small = i-1
		break
if(small == -1):
	print "No number exists"
	exit()
minNum = num[small+1]
minIndex = small+1
for j in range(small+1,len(num)):
	if(num[j] < minNum and num[j] > num[small]):
		minNum, minIndex = num[j],j
print small,minIndex
del num[minIndex]

num = num[:small]+[minNum]+sorted(num[small:])
print reduce(lambda x,y : x*10 + y, num)
