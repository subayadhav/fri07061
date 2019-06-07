a1,b,c=map(int,input().split())
if a1+b<=c or c+b<=a1 or a+c<=b:
	print("no")
else:
	print("yes")
