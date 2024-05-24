
a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
while b != 0:
    r = a % b
    a = b
    b = r
print("Greatest commom divisor: " + str(a))
    
