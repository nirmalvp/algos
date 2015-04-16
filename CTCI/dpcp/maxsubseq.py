num = map(int,raw_input("List :").split())
bestSoFar=num[0]
current=num[0]
for item in num[1:]:
	current=max(item,current+item)
	bestSoFar = max(bestSoFar,current)
print bestSoFar


