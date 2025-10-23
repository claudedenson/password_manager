def rot3_encrypt(new_record):
    # Provide simple rot3 encryption on all written data
    result = ""

    for char in new_record:
        if 'a' <= char <= 'z':
            result += chr(((ord(char) - ord('a') + 3) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr(((ord(char) - ord('A') + 3) % 26) + ord('A'))
        else:
            result += char  # Keep non-alphabetic characters unchanged

    return result

def rot3_decrypt(encrypted_record):

    # Decrypts text encrypted with the ROT3 cipher.
    result = ""
    for char in encrypted_record:
        if 'a' <= char <= 'z':
            result += chr(((ord(char) - ord('a') - 3 + 26) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr(((ord(char) - ord('A') - 3 + 26) % 26) + ord('A'))
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result