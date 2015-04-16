#finding the contiguous subarray within a one-dimensional array of numbers which has the largest sum
def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:] :
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
	return max_so_far

def mssl(A): # Arrays with only negative numbers are retured as 0
    best = cur = 0
    for i in A:
        cur = max(cur + i, 0)
        best = max(best, cur)
    return best

def msslWithIndex(A):
 	max_ending_here = subListStartIndex = max_so_far=0

 	for index,value in enumerate(A):
 		if(max_ending_here+value > 0):
 			max_ending_here += value
 		else:
 			max_ending_here, subListStartIndex = 0, index + 1
 		
 		if(max_ending_here>max_so_far):
 			startIndex,endIndex,max_so_far = (subListStartIndex, index+1, max_ending_here)

 	return (startIndex,endIndex,max_so_far)

theArray= [4, -2, -8, 5, -2, 7, 7, 2, -6, 5] 
startIndex,endIndex,max_so_far = msslWithIndex(theArray)

print "The subArray is ",theArray[startIndex:endIndex]
print "Maximum Sum is ", max_so_far	

