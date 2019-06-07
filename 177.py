l1=list(input().split())
a=[]
for i in range(len(l1)):
	a.append(sorted(l1[i]))
s=""
for i in a:
	s+="".join(i)+" "
print(s.strip())
	
