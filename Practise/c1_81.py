def printKeyCombs(digits,keymapping):
	if len(digits)==1 :
		for char in keymapping.get(digits):
			yield char
	else :
		currentDigit = digits[0]
		for previousChar in printKeyCombs(digits[1:],keymapping):
			for char in keymapping.get(currentDigit):
				yield char+previousChar
def main():
	keymapping =(	{"2": ["a","b","c"], 
			 	"3": ["d","e","f"], 
            	"4": ["g","h","i"], 
            	"5": ["j", "k","l"], 
            	"6": ["m","n", "o"], 
            	"7": ["p", "q", "r" ,"s"], 
            	"8": ["t", "u", "v"], 
            	"9": ["w", "x", "y" ,"z"]}) 
	print list(printKeyCombs(raw_input("Enter the digits wihtout spaces"),keymapping))
main()
