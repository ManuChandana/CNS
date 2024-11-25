import hashlib
def sha512(message):
    return hashlib.sha512(message.encode('utf-8')).hexdigest()
def display_header():
    print("=" * 40)
    print("           SHA-512 Hash Generator")
    print("=" * 40)
def display_footer():
    print("=" * 40)
    print("           Hashing Process Complete")
    print("=" * 40)
def main():
    display_header()
    message = input("Enter a message to hash: ")
    print("\nProcessing...")
    print("-" * 40)
    hash_value = sha512(message)
    print(f"Original Message: {message}")
    print("-" * 40)
    print("Generated SHA-512 Hash:")
    print(hash_value)
    print("-" * 40)
    display_footer()
if __name__ == "__main__":
    main() 
