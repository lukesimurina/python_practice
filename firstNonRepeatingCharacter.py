# Find the first non repeating character in a given string
# Cases:
#   "aabbcdd" --> "c"
#   "abcabcd" --> "d"
#   "abcabcabc" --> "_"

def firstNotRepeatingCharacter(s):
    for i in s:
        if s.index(i) == s.rfind(i):
            return i
    return "_"