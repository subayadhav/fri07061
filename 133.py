n1,k=map(int,input().split())
l=[]
c=0
for i in range(0,n1):
    l.append(list(map(int,input().split())))
for i in range(0,len(l)):
    if l[i][1]==k:
        c+=1
if c==0:
    print("no")
else:
    print("yes")
