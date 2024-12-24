def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    import string
    lower=string.ascii_lowercase
    i=0
    count=0
    while i<len(s):
        if s[i] in lower:
         count+=1
        i+=1
    return count
s='!@#$%1ASDF34'
print(main(s))