def encrypt(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    dir = False
    row, col = 0, 0
    for i in range(len(text)):
        if row == 0 or row == key - 1:
            dir = not dir
        rail[row][col] = text[i]
        col += 1
        row += 1 if dir else -1
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)
def decrypt(cipher, key):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    dir = None
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir = True
        if row == key - 1:
            dir = False
        rail[row][col] = '*'
        col += 1
        row += 1 if dir else -1
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir = True
        if row == key - 1:
            dir = False
        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1
        row += 1 if dir else -1
    return "".join(result)
plaintext = input("Enter Plaintext: ")
key = int(input("Enter Key: "))
ciphertext = encrypt(plaintext, key)
print("Encrypted Text:", ciphertext)
decrypted_text = decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)
