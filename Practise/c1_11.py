hours = input("Hour hand")
minutes = input("minutes hand")
hourAngle = (360/12) * hours + ( 360.0 / (12*60) ) * minutes
minutesAngle = (360/60) * minutes
print abs(hourAngle-minutesAngle)