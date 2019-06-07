s1=input()
n=int(s1,2)
x=n
while 1:
	if x&(x-1):
		x=x+1
	else:
		print(x)
		break
