def seive(limit):
	primes=[]
	for i in xrange(limit+1):
		primes.append(True)
	primes[0]= False
	primes[1] = False
	
	for num,isPrime in enumerate(primes):
		if(isPrime):
			yield num
			for indexOfMulitiples in xrange(num*2, limit+1, num):
				primes[indexOfMulitiples] = False

limit = int(raw_input("limit ; "))
for prime in seive(limit):
	print "%s\t"%prime,
