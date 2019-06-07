s1=list(input().split())
if len(s1)>1:
	for i in range(len(s1)):
		if s1[i]=='and':
			s1[i-1],s1[i+1]=s1[i+1],s1[i-1]
	print(*s1)
else:
	print(*s1)
