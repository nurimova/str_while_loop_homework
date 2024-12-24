def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    n=len(s)
    i=0
    count=0
    while i<n:
        if s[i].isdigit():
         count+=1
        i+=1
    return count
s='code 1234'
print(main(s))