# 75) The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

def createZigZag(sentence,rows):
	zigzag = [''] * rows
	listIndex = 0
	for char in sentence :
		zigzag[listIndex] += char
		if listIndex == 0 :
			forward = True
		elif listIndex == rows-1:
			forward = False
		listIndex += 1 if forward else -1
	return "".join(zigzag)

def main():
	sentence = raw_input("Enter the sentence")
	rows = input("Enter number of rows")
	print createZigZag(sentence,rows)
main()