#There is k parenthesis, write code to calculate how many permutations could have. 
        #For 2 parenthesis, there is 2 permutations: ()() and (()).
#http://en.wikipedia.org/wiki/Catalan_number#Applications_in_combinatorics
def countParenthesis(num):
	catalan = list()
	catalan.append(1)
	for n in range(num):
		catalanOfNPlusOne= ( 2 * (2*n+1) * catalan[n] ) / (n+2)
		catalan.append(catalanOfNPlusOne)
	return catalan[num]

print countParenthesis(input("enter number of parenthesis"))