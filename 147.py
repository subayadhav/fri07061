s1=list(map(str,input().split()))
for i in range(1,len(s1)):
    if i!=len(s1)-1:
        s1[i]=s1[i][::-1]
print(*s1)
