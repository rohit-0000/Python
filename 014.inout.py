#Writing a file
s="I am good boy."
# with open("test.txt","w") as f:
#     f.write(s)

# fp=open("test.txt","w")
fp=open("test.txt","a")  # for continuous writing without erasing
fp.write(s)
fp.close()

# Reading a file
# with open("test.txt","r") as d:
#     s=d.read()
#     print(s)

fr=open("test.txt","r")
print(fr.read())
fr.close()

