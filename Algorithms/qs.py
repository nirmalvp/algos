def qs(array):
	if not array:
		return list()
	pivot = array[0]
	smaller = [elem for elem in array[1:] if elem < pivot]
	larger = [ elem for elem in array[1:] if elem >= pivot]
	return qs(smaller) +[pivot]+ qs(larger)
