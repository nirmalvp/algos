#Given,
#n = number of people standing in a circle.
#k = number of people to count over each time
#Each person is given a unique (incrementing) id (0 to k-1). Starting with the first person (id 0), they begin counting 
#from 1 to k.
#The person at k is then removed and the circle closes up. The next remaining person (following the eliminated person) resumes counting at 1. 
#This process repeats until only one person is left, the winner.
#The solution must provide:the id of the winner.


def josephusProblemWinner(n,k):
	r = 0
	for i in range(2,n+1):
		r = (r + k) % i
	return r

n = input("Enter the number of people in the circle")
k = input("Enter Number of people to count over each time")

print josephusProblemWinner(n,k)
