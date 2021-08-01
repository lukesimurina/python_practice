# Find the first non repeating character in a given string
# Cases:
#   "aabbcdd" --> "c"
#   "abcabcd" --> "d"
#   "abcabcabc" --> "_"

def firstNonRepeatingCharacter(text):
    arr = list(text)
    arr1 = []
    for i in range(len(arr)):
        arr1.append(arr.count(arr[i]))
    try:
        print(arr[arr1.index(1)])
    except ValueError:
        print("_")