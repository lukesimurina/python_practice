def allLongestStrings(inputArray):
    m = max(len(i) for i in inputArray)
    return [i for i in inputArray if len(i) == m]