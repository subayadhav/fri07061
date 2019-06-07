m=int(input())
a1=list(map(int,input().split()))
b=list(map(int,input().split()))
if b[::-1]==a1:
  print("yes")
else:
  print("no")  
