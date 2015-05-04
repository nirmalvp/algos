#67) Given a string, print all the combinations with the chars in the string.
#        Example: for abc, the combinations are a, b, c, ab, ac, bc, abc.

def findCombinations(word,length):
	for index,letter in enumerate(word):
		if length == 1 :
			yield (letter,)
		else:
			 for previousCombination in findCombinations(word[index+1:],length-1):
			 	yield (letter,) + previousCombination
def main():
	for i,_ in enumerate(raw_input("Enter the word"),1):
		print list(findCombinations("abcd",i))
main()