n1=input()
c=0
for i in range(0,len(n1)):
    if int(n1[i])%2==1:
        c=c+int(n1[i])
if c%2==0:
    print("E")
else:
    print("O")
