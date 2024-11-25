import random
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result
def diffie_hellman(p, g):
    private_key_A = int(input("Enter Alice's private key: "))
    private_key_B = int(input("Enter Bob's private key: "))
    public_key_A = mod_exp(g, private_key_A, p)
    public_key_B = mod_exp(g, private_key_B, p)
    shared_secret_A = mod_exp(public_key_B, private_key_A, p)
    shared_secret_B = mod_exp(public_key_A, private_key_B, p)
    if shared_secret_A == shared_secret_B:
        return shared_secret_A
    else:
        return "Error: Shared secrets do not match!"
p = int(input("Enter a prime number (p): ")) 
g = int(input("Enter a base (g): "))
shared_secret = diffie_hellman(p, g)
if shared_secret == "Error: Shared secrets do not match!":
    print(shared_secret)
else:
    print(f"Shared Secret: {shared_secret}")
