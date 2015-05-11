def merge(list1,list2):
	i = 0
	j = 0
	mergedList=list()
	listOneLen = len(list1)
	listTwoLen = len(list2)
	while i<listOneLen and j < listTwoLen:
		if list1[i] < list2[j]:
			mergedList.append(list1[i])
			i+=1
		else :
			mergedList.append(list2[j])
			j+=1
	while i<listOneLen:
		mergedList.append(list1[i])
		i+=1
	while j< listTwoLen:
		mergedList.append(list2[j])
		j+=1
	return mergedList
def main():
	list1 = map(int,raw_input("Enter First sorted list").split())
	list2 = map(int,raw_input("Enter 2nd sorted list").split())
	print merge(list1,list2)
main()