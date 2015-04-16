from random import randint

def rand5():
	return randint(1,5)

while True:
	i = 5 * (rand5()-1) + rand5()
	if i <= 21:
		break

print (i%7 + 1)