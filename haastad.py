import sys
from data import e, c, n

sys.set_int_max_str_digits(25000)

# extended euclidean algorithm
def eea(a, b):
    q = [ -1, -1, -1]
    r = [ a, b, -1 ]
    s = [ 1, 0, -1 ]
    t = [ 0, 1, -1 ]
    i = 1
    while r[i % 3] != 0:
        i += 1
        j = i % 3
        k = (i - 1) % 3
        l = (i - 2) % 3
        q[j] = r[l] // r[k];
        r[j] = r[l] - q[j] * r[k]
        s[j] = s[l] - q[j] * s[k]
        t[j] = t[l] - q[j] * t[k]
    return (q, r, s, t, i)

# greatest common divisor
def gcd(a, b):
    _q, r, _s, _t, i = eea(a, b)
    return r[(i - 1) % 3]

# bézout's identity
def bezout(a, b):
    _q, _r, s, t, i = eea(a, b)
    return (s[(i - 1) % 3], t[(i - 1) % 3])

# chinese remainder theorem
def crt(a, n):
    x = a[0]
    N = n[0]
    for i in range(1, len(a)):
        x = _crt(x, a[i], N, n[i])
        N *= n[i]
    return x

def _crt(a1, a2, n1, n2):
    d = gcd(n1, n2)
    if d != 1:
        print(f'error: {n1} {n2} not coprime')
        exit()
    (m1, m2) = bezout(n1, n2)
    x = a1 * m2 * n2 + a2 * m1 * n1
    x %= (n1 * n2)
    return x

# fast ith root
def iroot(n, e):
    i = 1
    while (i ** e) <= n:
        i <<= 1

    i >>= 1
    root = i
    while i > 0:
        i >>= 1
        if ((root + i) ** e) <= n:
            root += i

    return root

# håstad's broadcast attack
def haastad(e, N, C):
    c = crt(C, N)
    M = iroot(c, e)
    return M

def to_bytes(n):
    out = []
    while n > 0:
        out.append(n & 0xff)
        n >>= 8;
    out.reverse()
    return out

def to_string(a):
    out = ""
    for c in a:
        out += chr(c)
    return out

M = haastad(e, n, c)
print(to_string(to_bytes(M)))
