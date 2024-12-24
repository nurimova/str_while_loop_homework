def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
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
        if s[i] in digit:
            count+=1
        i+=1
    return count
s='ASDfgh2345'
print(main(s))