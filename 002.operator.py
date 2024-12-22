# Arithmetic operator
num1=10
num2=3
print("num1 + num2 = ",num1+num2)
print("num1 - num2 = ",num1-num2)
print("|num1 - num2| = ",abs(num1-num2))
print("num1 * num2 = ",num1*num2)
print("num1 ^ num2 = ",num1**num2)   #  ** is exponential operator
print("num1 / num2 = ",num1/num2)
print("num1 // num2 = ",num1//num2)  # // its divide and gives integer value only
print("num1 % num2 = ",num1%num2)

#Assignment operator
'''
= is an assignment operator
'''
a=5
a+=2  # a=a+2
print(a)
a*=2  # a=a*2
print(a)
a-=2  # a=a-2
print(a)
a/=2  # a=a/2
print(a)
a//=2  # a=a//2
print(a)
a**=2  # a=a**2
print(a)

#comparision operator : it gives true or false

x=67
y=87
z=69
print(x>y)
print(x<y)
print(x==y)
print(x!=y)

#Logical Operator
print(x>y and x<z)
print(x>y or x<z)
print(not(x==y))
print(not(True))
print(not(False))

#Bitwise Operator
n1=0b101
n2=0b100

print(bin(n1&n2)) # bitwise and
print(bin(n1|n2)) # bitwise or
print(bin(n1^n2)) # bitwise xor
print(bin(~n1)) # bitwise not:- it represent in two`s compliment after operation of not
print(bin(n1>>1)) #bitwise right shift
print(bin(n1<<1)) #bitwise left shift