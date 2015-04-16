#There are ‘n’ ticket windows in the railway station, 
#ith window has ai tickets available. 
#Price of a ticket is equal to the number of tickets remaining in that window at that time. 
#When ‘m’ tickets have been sold, what’s the maximum amount of money the railway station can earn?
window = int( raw_input("Number of windows :") )
sold = int( raw_input("Number of tickets sold :") )
price=[]
for i in range(window):
	price.append(int( raw_input("Tickets available in window %s :" %(i+1)) ))
totalPrice = 0
for i in range(sold):
	maxIndex, maxPrice = max(enumerate(price), key = lambda x : x[1])
	price[maxIndex] -= 1
	totalPrice += maxPrice
print totalPrice
