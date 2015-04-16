m = int(raw_input("Enter no: of rows :"))
n = int(raw_input("Enter no: of rows :"))
mat=[]
zeroList=[]
def printMat(mat):
	for row in mat:
		for element in row:
			print "%s\t"%element,
		print "\n"

for i in range(m):
	row=[]
	for j in range(n):
		userInput = int(raw_input("Enter the mat[%s][%s]"%(i,j)))
		if(userInput == 0):
			zeroList.append((i,j))
		row.append(userInput)
	mat.append(row)
printMat(mat)

for x,y in zeroList:
	for i in range(m):
		mat[i][y] =0
	for j in range(n):
		mat[x][j] = 0

printMat(mat)




