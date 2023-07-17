def caesarCipherEncryptor(string, key):
    # Write your code here.
    new_word = ""
    while key > 26:
        key -= 26
    for char in string:
        if ord(char) + key > ord("z"):
            new_word += chr(ord(char) + key - 26)
        else:
            new_word += chr(ord(char) + key)
    return  new_word
