def gcd(a, b): 
    while b: 
        a, b = b, a % b
    return a
def extended_gcd(a, b):
    if a == 0: 
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    return g, y1 - (b // a) * x1, x1
def mod_inverse(e, phi):
    g, x, _ = extended_gcd(e, phi)
    return x % phi if g == 1 else None
p, q = int(input("Enter p (prime): ")), int(input("Enter q (prime): "))
n, phi = p * q, (p - 1) * (q - 1)
e = next(i for i in range(2, phi) if gcd(i, phi) == 1)
d = mod_inverse(e, phi)
if d is None:
    print("Invalid keys, modular inverse could not be found.")
else:
    msg = int(input("Enter a plaintext message (as an integer): "))
    if msg < n:
        c = pow(msg, e, n)
        decrypted_msg = pow(c, d, n)
        print("Public key: (e =", e, ", n =", n, ")")
        print("Private key: (d =", d, ", n =", n, ")")
        print("Encrypted message:", c)
        print("Decrypted message:", decrypted_msg)
    else:
        print("Message must be less than n =", n)
