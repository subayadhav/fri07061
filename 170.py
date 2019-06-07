ss=input()
g=[]
for i in ss:
	if i!=" ":
		g.append(ss.count(i))
m=max(g)
a=""
for i in ss:
	if ss.count(i)==m and i not in a:
		a=a+i
print(m,a)
