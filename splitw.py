dictwords = set(["how","are","you","a"])


def splitwords(sentence):
    n = len(sentence)
    if n==0:
        yield ""
    currentStr = ""
    for i in xrange(len(sentence)):
        currentStr+=sentence[i]
        if currentStr in dictwords:
            for words in splitwords(sentence[i+1:]):
                yield currentStr + " " + words




def main():
    print list(splitwords("howareyou"))
main()



