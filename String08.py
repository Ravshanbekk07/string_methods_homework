def main(s):
    """
    A variable of type str is given. Make sure it only consists of uppercase letters.
    Args:
        s: str
    Returns:
        bool: answer
    """
    
    return s == s.upper()

v = main("CODESCHOOL")
print(v)