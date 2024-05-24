a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
def gcd(a,b):
    r = a % b
    a = b
    b = r
    if b == 0:
        return a
    else:
        return gcd(a,b)
print (gcd(a,b))
