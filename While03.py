def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    import string
    punctuation=string.punctuation
    i=0
    count=0
    while i<len(s):
        if s[i] in punctuation:
         count+=1
        i+=1
    return count
s='!@#$%1234'
print(main(s))