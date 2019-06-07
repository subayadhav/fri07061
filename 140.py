s1=input()
if all(i=="a" or i=="b" for i in s1):
    print("yes")
elif all(i=="a" for i in s1):
    print("yes")
elif all(i=="b" for i in s1):
    print("yes")
else:
    print("no")
