def gcd(a, h):
    while True:
        temp = a % h
        if temp == 0:
            return h
        a, h = h, temp

p = int(input("Enter p: "))
q = int(input("Enter q: "))
n, phi, e = p * q, (p - 1) * (q - 1), 2
while e < phi:
    if gcd(e, phi) == 1: break
    e += 1
d = (1 + (2 * phi)) // e
msg = int(input("Enter message: "))
c = pow(msg, e, n)
m = pow(c, d, n)
print("Encrypted:", c)
print("Decrypted:", m)
