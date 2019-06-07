s1=input()
c=0
l=["a","e","i","o","u"]
for i in range(0,len(s1)-2):
	if s1[i] in l and s1[i+1] not in l:
		c+=2
		if s1[i+1] not in l and s1[i+2] in l:
			c+=1
print(c)
