l1=[3,53,36,7,8]
# it can strores multiple data type
# print(type(l1))
print(l1)
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[0:3])
l1.sort()
print (l1)

l1.remove(8)
print(l1)

l1.append(9)
print(l1)

l1.extend([200,400,56])
print(l1)

print(l1.count(2))

l1.pop()
print(l1)

print(l1.index(9))

l1[0]='rohit'
print(l1)

l1.clear()
print(l1)