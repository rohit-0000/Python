n=int(input("size"))
lst=[]
for i in range(0,n):
    lst.append(int(input()))
st=int(input("fst"))
last=int(input("last"))
for i in range(st,last):
    for j in range(st,last-i+st):
        if(lst[j]>lst[j+1]):
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)