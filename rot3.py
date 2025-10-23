
CHAR_SET="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, " 

# Provide simple rot3 encryption on all written data
def rot3_cypher(record, shift=3):
    
    # shift=3 encrypt
    # shift=-3 decrypt
    encText = "".join([CHAR_SET[(CHAR_SET.find(c)+shift)%94] for c in record]) 

    return encText