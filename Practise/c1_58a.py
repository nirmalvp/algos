#58A)Given a int N, write code to check if N is the power of 2.
def isPowerOfTwo(num):
	return num != 0 and num & (num-1) == 0  # num & (num-1) return 0(False) for power of Two but fails if num == 0.THis solves the prob
def main():
	num = input('Enter the num : ')
	print isPowerOfTwo(num)
main()