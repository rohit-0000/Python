def sum(a,b):
    return a+b

try:
    a, b = map(int, input().split())
    print(sum(a,b))
# except Exception as e:
#     print ("some error occurs",e)
except:
    print("some error occurs")