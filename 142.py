n1,k=map(int,input().split())
l=[]
for i in range(n1):
    l.append(input())
if l.count(l[i])==k:
    print("yes")
else:
    print("no")
