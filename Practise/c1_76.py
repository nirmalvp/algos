# -*- coding: utf-8 -*
def findNcK(numbers,k):
	for index,number in enumerate(numbers):
		if k == 1 :
			yield (number,)
		else :
			for prevComb in findNcK(numbers[index+1:],k-1):
				yield (number,) + prevComb

def allPossibleCombinations(numbers):
	for k in range(1,len(numbers)+1):
		print list(findNcK(numbers,k))

def addToSum(numbers,target,path):
	if target < 0 :
		return 
	if target == 0 :
		print path
		return
	for index,number in enumerate(numbers):
		newTarget = target-number
		path.append(number)
		addToSum(numbers[index:],newTarget,path[:])
		path.pop()

def main():
	#76A) Given a collection of numbers, return all possible combinations
	numbers = map(int,raw_input("Enter the numbers").split())
	allPossibleCombinations(numbers)
	
	#76C) Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C 
	#where the candidate numbers sums to T. 
	#The same repeated number may be chosen from C unlimited number of times. 
	#All numbers (including target) will be positive integers.  
	#Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak). 
	#The solution set must not contain duplicate combinations.  
	#For example, given candidate set 2,3,6,7 and target 7, A solution set is: [7], [2, 2, 3]

	numbers = map(int,raw_input("Enter the numbers").split())
	target = input("Enter the target Sum")
	addToSum(numbers,target,[])

main()








