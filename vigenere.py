def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return "".join(key)
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)
def encrypt(msg, key):
    e_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            e_c = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            e_c = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            e_c = char
        e_text.append(e_c)
    return "".join(e_text)
plaintext = input("Enter the message (plaintext): ")
key = input("Enter the key: ")
ciphertext = encrypt(plaintext, key)
print("Cipher text:", ciphertext)
