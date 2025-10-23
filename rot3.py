
CHAR_SET="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, " 

# Provide simple rot3 encryption on all written data
def rot3_encrypt(record):
    
    encText = "".join([CHAR_SET[(CHAR_SET.find(c)+3)%94] for c in record]) 

    return encText

# Decrypts text encrypted with the ROT3 cipher.
def rot3_decrypt(encrypted_record):

    encText = "".join([CHAR_SET[(CHAR_SET.find(c)-3)%94] for c in encrypted_record]) 

    return encText