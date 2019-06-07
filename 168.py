ss=input()
l=[]
for i in range(len(ss)):
	if ss[i].isdigit():
		l.append(ss[i-1]*(int(ss[i])-1))
	else:
		l.append(ss[i])
print("".join(l))
