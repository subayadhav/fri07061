s1=input()
i=0
k=""
j=i+1
c=1
while j<len(s1):
	if s1[i]==s1[j]:
		c=c+1
	else:
		k=k+s1[i]+str(c)
		i=j
		c=1
 
	j=j+1
k=k+s1[i]+str(c)
print(k)
