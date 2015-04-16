uniqString = raw_input("Enter the String") 
checker = 0
flag=0
for ch in uniqString:
	val = ord(ch) - ( ord('a') if ch.islower() else ord('A') )
	if( checker & (1<<val) != 0 ):
		flag = 1 
	checker = checker | (1<<val)
if(flag == 1):
	print "Not Unique"
else :
	print "Unique"


