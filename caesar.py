def caesar_encrypt(plaintext, shift):
    result = ""
    for i in plaintext:
        if(i==" "):
            result+=" "
        elif(i.isdigit()):
            result+=i
        elif(i=='z'or i=='Z'):
            result+=chr((ord(i)-26)+shift)
        else:
            result+=chr(ord(i)+shift)
    return result
plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift value (integer): "))
ciphertext = caesar_encrypt(plaintext, shift)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")