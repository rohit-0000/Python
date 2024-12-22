a="rohit"
print(a)
print(a[0:4])     #print from 0 to 4 ie rohi
print(a[2:4])     #print from 2 to 4 ie hi
print(a.upper())  #print in upper case
print(a.capitalize())  #print first letter in upper case
print(a.count('r')) #count the number of char pesent in string
print(a.isnumeric()) #check the string is numeric or not
ab="56"
print(ab.isnumeric()) #check the string is numeric or not
print(a.isalnum()) #check string is alphabet or numberic
b="i am rohit\n" \
  "i am rohit"   # \--> helps in multiline strings
print(b)

s1=f"this is f string and my name is {a}"
print(s1)