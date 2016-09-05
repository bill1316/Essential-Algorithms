a=567
b=234

def gcd(a,b):
    if b==0:
       return a
    else:
       return gcd(b, a%b)

print gcd(a,b)
