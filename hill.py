import numpy as np
def getKeyMatrix(key): return np.array([[ord(key[i*3+j])%65 for j in range(3)] for i in range(3)])
def encrypt(message, key):
 keyMatrix=getKeyMatrix(key)
 messageVector=np.array([[ord(char)%65] for char in message])
 cipherMatrix=np.dot(keyMatrix,messageVector)%26
 return ''.join(chr(int(num)+65) for num in cipherMatrix.flatten())
message=input("Enter the message (3 characters): ").upper()
key=input("Enter the key (9 characters): ").upper()
if len(message)==3 and len(key)==9:
 print("Ciphertext:",encrypt(message,key))
else:
 print("Error: Message must be 3 characters long, and key must be 9 characters long.")
