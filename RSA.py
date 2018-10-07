### RSA algorithm implementation



# define functions
def check_prime(n):                # check if the number n is prime
    if n <= 1:
        print("the number",n,"is not prime")
        return False
    else:
        for i in range(2, n):
            if n%i == 0:
                print("the number",n,"is not prime")
                return False
        else:
            print("the number",n,"is prime")
            return True

def find_e(k):                    # find the parameter e
    e = 2
    while True:
        if find_gcd(e, k) == 1:
            return e
        e+=1

def find_gcd(p, q):               # find the greatest common divisor using Euclid algorithm
    a=[]
    b=[]
    c=[]
    d=[]
    while q != 0:
        a.append(p)
        b.append(q)
        c.append(p//q)
        d.append(p%q)
        p, q = q, p%q
        if q == 0:
            break
    gcd = b.pop()
    return gcd

def extEuclidAlg(p, q):           # Extended Euclid algorithm
    a=[]
    b=[]
    c=[]
    d=[]
    while q != 0:
        a.append(p)
        b.append(q)
        c.append(p//q)
        d.append(p%q)
        p, q = q, p%q
        if q == 0:
            break
    a.pop()
    gcd = b.pop()
    c.pop()
    d.pop()    
    a.reverse()
    b.reverse()
    c.reverse()
    d.reverse()
    for i in range(len(a)):
        if i == 0:
            x = a[0]
            n = 1
            y = b[0]
            m = -c[0]
        else:
            x,n,y,m = a[i],m,b[i],-c[i]*m+n 
    return n, m

def find_d(a, m):                # find the parameter d
    x, y = extEuclidAlg(a, m)
    return x%m



# main

while True:                      # input p
    p = input("\nEnter a prime number p: ")
    if p == "":
        p = 3
    else:
        p = int(p)
    if check_prime(p):
        break

while True:                     # input q
    q = input("\nEnter a prime number q: ")
    if q == "":
        q = 7
    else:
        q = int(q)
    if check_prime(q):
        break

# calculate parameters n and k
n = p*q
print("\nparameters:\nn =", n)
k = (p-1)*(q-1)
print("k =", k)

# calculate parameter e and d
e = find_e(k)
print("e =", e)
d = find_d(e, k)
print("d =", d)

# generate public key and private key
print("\npublic key: (", n, ",", e, ")")
print("private key: (", n, ",", d, ")")
print("***********************************************\n")

# Encrypt a character m using the public key, output c
m_str = input("Enter a character you want to encrypt: ")

# default
if m_str == "":
    m_str = "b"
    
print("messege =", m_str)
m = ord(m_str.lower())-97
c = (m**e)%n
if c <= 26:
    c = chr(ord('a') + c)
print("code =",c)

# Decrypt c using the private key, output m
c_str = input("Enter a number or character you want to decrypt: ")

# default
if c_str == "":
    c_str = "5"
    
print("code =", c_str)
try:
    m = (int(c_str)**d)%n
except:
    m = ((ord(c_str)-97)**d)%n
m = chr(ord('a') + m)
print("messege =", m)
