a1,b=map(str,input().split())
if a1==b:
	print("D")
elif (a1=="R" and b=="P") or (a1=="P" and b=="R"):
	print("P")
elif (a1=="S" and b=="P") or (a1=="P" and b=="S"):
	print("S")
elif (a1=="S" and b=="R") or (a1=="R" and b=="S"):
	print("R")
