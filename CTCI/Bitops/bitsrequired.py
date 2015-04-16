num1 = int(raw_input("number 1 : "))
num2 = int(raw_input("number 2 : "))
diff = num1 ^ num2
count = 0
while (diff!=0):
	if(diff & 1 !=0):
		count+=1
	diff = diff>>1
print count
