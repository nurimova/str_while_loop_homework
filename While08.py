def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    import string
    digit=string.digits
    i=0
    count=0
    while i<len(s):
        if s[i] in digit and int(s[i])%2==0:
            count+=1
        i+=1
    return count
s='23 df 45 g67'
print(main(s))