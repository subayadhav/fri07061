n1=int(input())
s=bin(n1)[2::]
a=s[::-1]
print(a.index("1")+1)
