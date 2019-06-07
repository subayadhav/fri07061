s=input()
r1=input()
g=[]
if (s.isalpha() or " " in s) and (r1.isalpha() or " " in r1):
    s=list(s.split(" "))
    r1=list(r1.split(" "))
    for i in s:
        if s.count(i) > r1.count(i) and i not in g:
            g.append(i)
    for i in r1:
        if r1.count(i)>s.count(i) and i not in g:
            g.append(i)
    print(*g)
else:
    for i in s:
        if s.count(i)>r1.count(i) and i not in g:
            g.append(i)
    for j in r1:
        if r1.count(j)>s.count(j) and j not in g:
            g.append(j)
    print(*g)
