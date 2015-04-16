stringOne = raw_input("Enter String 1 :")
stringTwo = raw_input("Enter String 2 :")

wordCount ={i:stringOne.count(i) for i in stringOne}
flag = 0
for ch in stringTwo:
	if(wordCount.get(ch) == None):
		flag = 1
	else:
		wordCount[ch] -= 1

for value in wordCount.values():
	if(value!=0):
		flag=1

if(flag==1):
	print "Not Anagram"
else:
	print "Anagram"