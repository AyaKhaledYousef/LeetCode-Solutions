# l=[6,5,4,3,2,1]
# d=2
# total=[]
# for i in l:
#     print(i)
#     d1=l[:i]
#     print("D1=",d1,"Sum=",max(d1))
#     print(d1)
#     d2=l[i:]
#     if not d2:
#         continue
#     print("D2=",d2,"Sum=",max(d2))
#     total.append(max(d1)+max(d2))
#     print("Total=",total)
#     print("******************")
# print("final=",min(total))
    
from pickletools import string1, string4


d=3
l=[8,2,3,4,5,6,7,8,6]
for x in range(1, d+1):
    globals()['string%s' % x] = l[:d]
print(string1)
print(string2)
print(string3)

string1=l[:d]
string2=l[d:d]
string3=l[:d]