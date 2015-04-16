# -*- coding: utf-8 -*-
#Given a set T of characters and a string S,
#find the minimum window in S which will contain all the characters in T in complexity O(n).
#S = “ADOBECODEBANC”
#T = “ABC”
#Minimum window is “BANC”

sourceString = raw_input('Enter the source string : ')
subString = raw_input('Enter the substring : ')
minWindow = len(sourceString)+1 # An unattainable value
minWindowBegin =0
minWindowEnd =0
needToFind = {x:subString.count(x) for x in subString}
hasFound={x:0 for x in needToFind.keys()}
count = 0
begin = 0
for end in range(len(sourceString)) :
	letter = sourceString[end]
	if(needToFind.get(letter) == None):
		continue
	hasFound[letter] += 1
	if(hasFound[letter] <= needToFind[letter]):
		count += 1
	if(count == len(subString)):
		firstLetter = sourceString[begin]
		while(needToFind.get(firstLetter) == None or hasFound[firstLetter]>needToFind[firstLetter]):
			if(hasFound.get(firstLetter) > needToFind.get(firstLetter)):
				hasFound[firstLetter] -= 1
			begin += 1
			firstLetter = sourceString[begin]
		currentWindow = (end - begin) + 1
		if(currentWindow<minWindow):
			minWindow = currentWindow
			minWindowBegin = begin
			minWindowEnd = end
		
if(minWindow ==  len(sourceString)+1 ):
	print "No string found"
else :
	print "Minimum Window is ",sourceString[minWindowBegin:minWindowEnd+1]
	print "Range :",minWindowBegin,minWindowEnd

