#66) You are given two sorted arrays, A and B, 
#where A has a large enough buffer at the end to hold B. Write method to merge B into A.
def merge(a,b,a_tail,b_tail,a_end):
	while a_tail >=0 and b_tail >=0 :
		if b[b_tail] > a[a_tail] :
			a[a_end] = b[b_tail]
			b_tail -=1
		else :
			a[a_end] = a[a_tail]
			a_tail -=1
		a_end -= 1
	
	while b_tail>=0 :
		a[a_end] = b[b_tail]
		b_tail -=1
		a_end -=1

def main():
	a = map(int,raw_input("Enter the first sorted array").split())
	a_tail = len(a) - 1
	b = map(int,raw_input("Enter the second sorted array").split())
	b_tail = len(b) - 1
	a = a + [None for _ in b]
	a_end = len(a) - 1
	merge(a,b,a_tail,b_tail,a_end)
	print a
main()