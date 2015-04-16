#12) Design a algorithm to point all permutation of a string, assume all the character are unique  same as C11_4

def findPermutation(word):
    if len(word) == 1:
        yield word
    else:
        firstChar = word[0]
        prevPermutations = findPermutation(word[1:])
        for permutation in prevPermutations:
            for pos in range(len(permutation)+1):
                yield ( permutation[:pos] + firstChar + permutation[pos:] )
    
word = raw_input("Enter String : ")
print list(findPermutation(word))
