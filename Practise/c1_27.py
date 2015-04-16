def combination(iterable,r):
	for pos,element in enumerate(iterable):
		if r==1 :
			yield tuple([element]) #single element tuple
		else :
			currentElement = tuple([element])
			for prevCombination in combination( iterable[pos+1:len(iterable)] , r-1 ):
				yield currentElement + prevCombination
	

