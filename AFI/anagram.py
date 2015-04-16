import string
from collections import defaultdict
with open("wordsEn.txt") as f:
	a=f.read()
myDict=set(a.split())
anagram = defaultdict(list)
for word in myDict:
	sortedWord = "".join(sorted(word))
	anagram[sortedWord].append(word)

for value in anagram.values():
	if(len(value)>1):
		print value