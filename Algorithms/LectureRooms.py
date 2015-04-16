
#Suppose we have a set of activities to schedule among a large number of lecture halls.
#We wish to schedule all the activities using as few lecture halls as possible
#Find minimum number of lecture Rooms required
lectures = [(0,2),(1,3),(3,5),(4,6)] #(startTime, finishTime) tuples
#Indexes to the two elements in tuple for more readable code
startTime = 0 
finishTime = 1
#Sort according to startTime
lectures = sorted(lectures) 
lectureRooms=[]
#Store finish time of the first lecture
lectureRooms.append(lectures[0][finishTime])  
for lecture in lectures[1:] :
	#Sort lecture rooms so that the room with smallest finish time is at 0 position
	lectureRooms = sorted(lectureRooms)
	if(lectureRooms[0] > lecture[startTime] ): 
		#if the room with smallest finish time already has a greater finish time than the start time of the lecture, 
		#it cant be accomodated in any existing rooms
		lectureRooms.append(lecture[finishTime])
	else :
		lectureRooms[0] = lecture[finishTime]
print len(lectureRooms)