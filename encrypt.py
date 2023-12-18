import random, sys

# greatest common divisor
def gcd(a, b):
    r = [ a, b, -1 ]
    i = 1
    while r[i % 3] != 0:
        i += 1
        r[i % 3] = r[(i - 2) % 3] % r[(i - 1) % 3]
    return r[(i - 1) % 3]

# probabilistic fermat primality test
def is_prime(n):
    ITER = 100
    BITS = 2 ** 6

    i = 0
    while i < ITER:
        a = random.getrandbits(BITS)
        if (gcd(a, n) != 1): return False;
        r = pow(a, n - 1, n)
        if (r != 1): return False
        i += 1

    return True

def get_prime(bits):
    print("searching for prime...")
    while True:
        rand = random.getrandbits(bits)
        if (is_prime(rand)):
            print("found!")
            return rand

def to_bytes(string):
    out = []
    for c in string:
        out.append(ord(c))
    return out

def to_int(bytes):
    bytes.reverse()
    out = 0
    for i in range(len(bytes)):
        out += 256 ** i * bytes[i]
    return out

bits = 512
secret = sys.argv[1]
m = to_int(to_bytes(secret))
f = open ("data.py", "w")
e = 37
n = [get_prime(bits) * get_prime(bits) for i in range(e)]
c = [pow(m, e, n[i]) for i in range(e)]

with open ("data.py", "w"):
    f.write(f"e = {e}\n")
    f.write(f"c = {c}\n")
    f.write(f"n = {n}\n")
