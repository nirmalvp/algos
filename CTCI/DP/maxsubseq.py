num = map(int,raw_input("List :").split())

def maxsubseq():
	bestSoFar=num[0]
	current=num[0]
	for item in num[1:]:
		current=max(item,current+item)
		bestSoFar = max(bestSoFar,current)
	print bestSoFar

def maxsubseqwithIndex():
	bestSoFar=num[0]
	current=num[0]
	start = 0
	end = 0
	for index,item in enumerate(num[1:],1):
		if(item >= current+item):
			current=item
			start = index
		else:
			current = current+item
		if(current >= bestSoFar):
			bestSoFar = current
			end = index
	print num[start:end+1]

maxsubseq()
maxsubseqwithIndex()




