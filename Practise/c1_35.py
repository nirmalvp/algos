#Write a function to print out all the amicable numbers pair within 10000;
 #           amicable numbers pair is the numbers which the sum of its real factor equals to the other. such as 220 and 284
def findSumOfFactors(num):
    sumofFactor = 0
    for factor in range(1,num):
        if num % factor ==0:
            sumofFactor += factor
    return sumofFactor  


def amicablePairs():
    sumdict=dict()
    for num in xrange(10001):
        sumofFactor = findSumOfFactors(num)
        sumdict[num] = sumofFactor 
        if sumofFactor < num:
            if sumdict[sumofFactor] == num:
                yield (sumofFactor,num)
print list(amicablePairs())