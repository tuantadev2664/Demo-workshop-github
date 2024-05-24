a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
def gcd(a, b):
    if(b == 0):
        return a
    if(a > b):
        return gcd(b, a % b)
    elif(a == b):
        return abc
    else:
        return gcd(a, b % a)
    
print(gcd(a,b))

print("hihi")