def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    import string
    upper=string.ascii_uppercase
    i=0
    count=0
    while i<len(s):
        if s[i] in upper:
         count+=1
        i+=1
    return count
s='!@#$%1ASDF34'
print(main(s))