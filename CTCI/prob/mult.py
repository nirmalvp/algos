k = int(raw_input("K :"))
x=1
q3=[]
q5=[]
q7=[]
for i in range(k):
	q3.append(x*3)
	q5.append(x*5)
	q7.append(x*7)

	x=min(q3[0],q5[0],q7[0])
	if (x==q3[0]):
		q3.pop(0)
	if (x==q5[0]):
		q5.pop(0)
	if (x==q7[0]):
		q7.pop(0)

	print x






