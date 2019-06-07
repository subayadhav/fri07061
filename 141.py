n1=int(input())
l=[]
for i in range(n1):
    l.append(input())
if all(l[i]==l[i+1] for i in range(len(l)-1)):
    print("yes")
else:
    print("no")
