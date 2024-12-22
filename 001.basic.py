print("hello world");

# # def hexa_to_binary(hex):
# #     hexa="0123456789ABCDEF"
# #     no=0
# #     power=0
# #     for i in reversed(hex):
# #         no=no+hexa.index(i)*(16**power)
# #         power=power+1
# #
# #     bin=""
# #     while(no>0):
# #         bin=str(no%2)+bin;
# #         no=no//2;
# #     return bin
# #
# # def hexa_to_octal(hex):
# #     hexa="0123456789ABCDEF"
# #     no=0
# #     power=0
# #     for i in reversed(hex):
# #         no=no+hexa.index(i)*(16**power)
# #         power=power+1
# #
# #     oct=""
# #     while(no>0):
# #         oct=str(no%8)+oct;
# #         no=no//8;
# #     return oct
# #
# # list=[]
# # print("Enter 10 hexadecimal no :")
# # for i in range(0,10):
# #     list.append(input().upper())
# # for i in range (0,10):
# #     ck=input(f"Choose the conversion octal or binary for no{1+i}").upper()
# #     if ck=="BINARY":
# #         print(hexa_to_binary(list[i]))
# #     elif ck=="OCTAL":
# #         print(hexa_to_octal(list[i]))
# #
#
# import math
#
#
# #
#
#
# # lst=[]
# # sum=0
# # sz=int(input("Enter size of list"))
# # print(f"Enter {sz} number : ")
# # for i in range(0,sz):
# #     lst.append(int(input()))
# #     sum=sum+lst[i];
# # print(f"sum of all element in a list = {sum}")
# # print(f"average of all element in a list = {sum/sz} ")
# # lo=int(input("Enter the lower(index) range for sum and average "))
# # hi=int(input("Enter the higher(index) range for sum and average "))
# # sum1=0
# # for i in range(lo,hi+1):
# #     sum1=sum1+lst[i]
# # print(f"sum of  element in a list  from index {lo} to {hi} = {sum1}")
# # print(f"average of element in a list from index {lo} to {hi} = {sum1/(hi-lo+1)} ")
#
#
# # def prime(no):
# #     for i in range(2,int(math.sqrt(no)+1)):
# #         if(no%2==0):
# #             return False
# #     return True
# # yrs=[]
# # for i in range(0,10):
# #     yrs.append(int(input()))
# # ans=[]
# # for i in yrs:
# #     if(prime(i)==True):
# #         ans.append(i)
# # print(f"List of prime years from List yrs is {ans}")
#
#
# # def octal_to_binary(octal):
# #     no=0
# #     power=0
# #     for i in reversed(octal):
# #         no=no+int(i)*(8**power)
# #         power=power+1
# #     bin=""
# #     while(no>0):
# #         bin=str(no%2)+bin;
# #         no=no//2;
# #     return bin
# # def octal_to_hexa(octal):
# #     no=0
# #     power=0
# #     for i in reversed(octal):
# #         no=no+int(i)*(8**power)
# #         power=power+1
# #     hexa="0123456789ABCDEF"
# #     hex=""
# #     while(no>0):
# #         hex=hexa[no%16]+hex;
# #         no=no//16;
# #     return hex
# # list=[]
# # print("Enter 10 octal no :")
# # for i in range(0,2):
# #     list.append(input())
# # for i in range (0,10):
# #     ck=input(f"Choose the conversion hexa or binary for no{1+i}").upper()
# #     if ck=="BINARY":
# #         print(octal_to_binary(list[i]))
# #     elif ck=="HEXA":
# #         print(octal_to_hexa(list[i]))
# #
# # Example usage:
# # lst = []
# # n=int(input())
# # for i in range(0,n):
# #     lst.append(int(input()))
# # target = int(input("Enter target value"))
# # start =int(input("Enter starting range"))
# # end = int(input("Enter ending range"))
# #
# # result =-1;
# # for i in range(start, end + 1):
# #     if lst[i] == target:
# #        result=i;
# #
# #
# # if result != -1:
# #     print(f"Target {target} found at index {result} in the range [{start}, {end}]")
# # else:
# #     print(f"Target {target} not found in the range [{start}, {end}]")
#
# #def palin(s):
# #     for i in range(0,len(s)):
# #         if(s[i]!=s[len(s)-i-1]):
# #             return False;
# #     return True
# #
# # lst_str=[]
# # ans=[]
# # n=int(input())
# # for i in range(n):
# #     lst_str.append(input())
# #     if(palin(lst_str[i])):
# #         ans.append(lst_str[i])
# # print(ans)
#
# def ck_vowel(s):
#     for i in s:
#         if(i=='a'or i=='e' or i=='i' or i=='o' and i=='u'):
#             return True
#     return False
# lst=[]
# ans=[]
# n=int(input())
# for i in range(n):
#     lst.append(input())
#     if(ck_vowel(lst[i])):
#         ans.append(lst[i])
# print(ans)
#
#
# # def sum(no):
# #     s=0
# #     while(no>0):
# #         s+=(no%10)
# #         no=no//10
# #     return s
#
# # lst=[]
# # n=int(input())
# # for i in range(n):
# #     lst.append(int(input()))
# # lst_sum=[]
# # for i in lst:
# #     lst_sum.append(sum(i))
# # dict={}
# # for i in lst:
# #     dict[i]=lst_sum[lst.index(i)]
# # print(dict)

