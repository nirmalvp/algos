#59) Write code to get N prime numbers

def sievePrimeUptoN(n):
	sieve = [True] * (n+1)
	sieve[0] = False
	sieve[1] = False
	for number, isPrime in enumerate(sieve):
		if isPrime:
			yield number
			for otherIndex in range(number*2,n+1,number):
				sieve[otherIndex] = False

def main():
	n = input("Enter N : ")
	print list(sievePrimeUptoN(n))
main()

