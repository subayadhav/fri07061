n1=int(input())
l=[]
a=0
for i in range(2,n1//2):
	if n1%i==0:
		for j in range(2,i//2+1):
			if i%j==0:
				a=1
				break
		if a!=1:
			l.append(i)
		a=0
print(*l,sep=' ')
