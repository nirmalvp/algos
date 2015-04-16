def nQueens(row,queen,n):
	q=queen[:]
	if(row == n ):
		print q
		return 
	for col in range(n):
		if(noAttack(q,row,col)):
			q[row] = col
			nQueens(row+1,q,n)
			q[row] = None

def noAttack(queen,row,col):
	for otherRow in range(row):
		if(queen[otherRow]==col):
			return False
		if( abs(row-otherRow) == abs(col-queen[otherRow]) ):
			return False
		#else:
		#	if(row==2 and col==1):
		#		print otherRow,queen
	return True
n = int(raw_input("Input the Board Size : Example : 8 :"))
queen=[None]*n
nQueens(0,queen,n)





