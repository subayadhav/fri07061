s1,k=input().split()
k=int(k)
l=[]
for i in range(k-1,len(s1),k):
    l.append(s1[i])
print(*l)
