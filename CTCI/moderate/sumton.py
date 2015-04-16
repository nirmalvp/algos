myArray = map(int, raw_input("Enter the numbers in the list : ").split())
requiredSum = input("Enter the requiredSum : ")

def usingsort():
    sortedArray =sorted(myArray)
    low = 0
    high = len(sortedArray)-1
    while(low<=high):
        elementSum =sortedArray[low]+sortedArray[high]
        #print sortedArray[low],sortedArray[high],elementSum
        if(elementSum == requiredSum):
            print sortedArray[low],sortedArray[high]
            low +=1
            high -=1
        elif elementSum > requiredSum:
            high = high - 1
        else :
            low = low+1
def withoutsort():
    myDict=dict()
    for item in myArray:
        otherElement = requiredSum-item
        if(not myDict.get(otherElement)):
            myDict[otherElement] = 1
        else :
            myDict[otherElement] +=1
    for item in myArray:
        if myDict.get(item):
            myDict[item] -= 1
            if (item<=requiredSum-item):
                print item,requiredSum-item
print "Using sort"
usingsort()
print "Without Using sort"
withoutsort()
