n1,p=map(int,input().split())
k=n1*p
s=bin(k)
for  i in range(0,len(s)):
    if s[i]=='1':
        print(i+1)
        break
