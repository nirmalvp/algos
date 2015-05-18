#53) Given an int array A and a sliding window width w, scan the array with sliding window and keep the max value in the window to array B.
#Write code to find B. B[i] should be the max value among A[i] ~ A[i + w - 1];
#http://www.geeksforgeeks.org/maximum-of-all-subarrays-of-size-k/
from collections import deque
def maxInSLidingWindow(array,windowLength):
	maxQueue = deque([])
	for index,element in enumerate(array[:windowLength]):
		while maxQueue and element > array[maxQueue[0]]:
			maxQueue.popleft()
		maxQueue.appendleft(index)
	yield array[maxQueue[-1]]

	for index,element in enumerate(array[windowLength:],windowLength):
		while maxQueue and index - maxQueue[-1] >= windowLength :
			maxQueue.pop()
		while maxQueue and element > array[maxQueue[0]]:
			maxQueue.popleft()
		maxQueue.appendleft(index)
		yield array[maxQueue[-1]]

def main():
	array = map(int,raw_input("Enter the array :  ").split())
	windowLength = input("Enter the length of the window :  ")
	print list(maxInSLidingWindow(array,windowLength))
main()