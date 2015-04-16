hour = int(raw_input("hour :"))
mins = int(raw_input("mins: "))

minAngle = 360/60 * mins
print minAngle
hourAngle = (360/12 * (hour % 12) ) + (360.0/(12*60) * mins)
print hourAngle
diff = minAngle - hourAngle

print diff if diff>0 else -diff