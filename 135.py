n1=int(input())
l=[int(x) for x in input().split()]
if n1%2!=0:
    m=(n1-1)//2
    a=sorted(l[0:m])
    b=sorted(l[m:])
    s=a+b[::-1]
    print(*s)
else:
    m=n//2
    a=sorted(l[0:m])
    b=sorted(l[m:])
    s=a+b[::-1]
    print(*s)
