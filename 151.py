s1=input()
b=[]
for i in s1:
    if i!="a" and i!="b":
        b.append(i)
if all(i=="a" or i=="b" for i in s1):
    print("yes")
elif all(i=="a" for i in s1):
    print("yes")
elif all(i=="b" for i in s1):
    print("yes")
elif len(b)==1:
    print("yes")
else:
    print("no")
