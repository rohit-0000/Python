
# def sum():
#     a,b=map(int,input().split())
#     print ("sum of ",a,"+",b," = ",a+b)

# func

def sum(a=0,b=0):
    print (a+b)
def subt(a=0,b=0):
    print(abs(a-b))
def mult(a=1,b=1):
    print (a*b)
def divide(a,b):
    return a/b
x,y=map(int,input().split())
sum(x,y)
subt(x,y)
mult(x,y)
print(divide(x,y))