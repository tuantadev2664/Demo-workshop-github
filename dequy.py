a = int(input("Enter num1: ")) 
b = int(input("Enter num2: "))
def gcd(a, b):
    if(b == 0):
        return a
    if(a > b):
        return gcd(b, a % b)
<<<<<<< HEAD
    elif(a == b):
        return abc
=======
    elif(a != b):
        return a
>>>>>>> bdfe6c7c4ce7aa37c202612cce741e7b4359f489
    else:
        return gcd(a, b % a)
    
print(gcd(a,b))

print("hihi")