# a={}
# print(type(a))
# b=set()
# print(type(b))

dict1 ={"good":"something pleasant","fetch":"to bring","1":"The number 1"}
marks={"harshit":34,"harry":99,"rohit":100,"shivani":33}
print(dict1["good"])
print(marks["rohit"])

print(marks.get("pryinka chopra"))
# print(marks["pryinka chopra"]) #pryinka chopra is not in dictionary thats why show error to avoid error use get function

marks["arpit"]=56
print(marks)

marks.pop("arpit")
print(marks)

print(marks.keys())
print(marks.values())
print(marks.items())

marks.clear()
print(marks)

