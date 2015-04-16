num = int(raw_input("Enter num : "))
swapped = (num<<1) | (num>>1)
print bin(num),"-->",bin(swapped)