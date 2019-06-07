s1=input()
k=""
for i in s1:
	if s1.count(i)>1:
		k=k+i.upper()
	else:
		k=k+i
print(k)
