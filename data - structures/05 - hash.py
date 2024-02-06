def simple_hash(s):
    hash_code = 0
    for char in s:
        hash_code += ord(char)
    # ord() returns the ASCII value of a character
    return hash_code
