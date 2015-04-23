#42) We call the number which factors only include 2,3,5 as "Ugly Number". Write code to compute 1500 ugly number.
from collections import deque
twoQ = deque([2])
threeQ =deque([3])
fiveQ = deque([5])

for i in range(1500):
	uglyNum = min(twoQ[0],threeQ[0],fiveQ[0])
	if twoQ[0] == uglyNum:
		twoQ.popleft()
	if threeQ[0] == uglyNum:
		threeQ.popleft()
	if fiveQ[0] == uglyNum:
		fiveQ.popleft()
	twoQ.append(uglyNum*2)
	threeQ.append(uglyNum*3)
	fiveQ.append(uglyNum*5)
	print uglyNum, 
