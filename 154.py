s1,k=input().split()
k=int(k)
a=""
for i in range(len(s1)):
    if (i+1)%k==0:
        a+=s1[i].upper()
    else:
        a+=s1[i]
print(a)
