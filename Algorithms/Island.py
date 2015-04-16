# -*- coding: utf-8 -*-
#Given a rectangular matrix which has only two possible values ‘X’ and ‘O’.
#The values ‘X’ always appear in form of rectangular islands and 
#these islands are always row-wise and column-wise separated by at least one line of ‘O’s. 
#Note that islands can only be diagonally adjacent.
#Count the number of islands in the given matrix.

islandMap = [['O', 'O', 'O'],
             ['X', 'X', 'O'],
             ['X', 'X', 'O'],
             ['O', 'O', 'X'],
             ['O', 'O', 'X'],
             ['X', 'X', 'O']
            ]
countIslands = 0
for i in range(len(islandMap)):
	for j in range(len(islandMap[0])):
		if( islandMap[i][j] != 'X'):
			continue
		if( (i==0 or islandMap[i-1][j]=="O") and (j==0 or islandMap[i][j-1] == 'O')):
			countIslands+=1
print "Number of islands : ",countIslands



