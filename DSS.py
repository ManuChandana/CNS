from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
def generate_keys():
    private_key = dsa.generate_private_key(key_size=2048)
    return private_key, private_key.public_key()
def sign_message(private_key, message):
    return private_key.sign(message, hashes.SHA256())
def verify_signature(public_key, message, signature):
    return public_key.verify(signature, message, hashes.SHA256()) is None
if __name__ == "__main__":
    message = input("Enter message: ").encode()
    private_key, public_key = generate_keys()
    signature = sign_message(private_key, message)
    print("Message:", message.decode())
    print("Signature:", signature.hex())
    print("Signature valid:", verify_signature(public_key, message, signature))
