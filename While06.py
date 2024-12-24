def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    import string
    consonat=['a','e','i','o','u']
    i=0
    count=0
    while i<len(s):
        if s[i] in consonat:
         count+=1
        i+=1
    return count
s='asdgh 23s'
print(main(s))