n1,k=map(int,input().split())
r=n1*k
s=bin(r)[2::]
a=s[1:]
b=a.index("1")
print(b+2)
