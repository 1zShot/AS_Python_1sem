s=input()
r=""
i=0
while i <len(s):
    c=s[i]
    n=1
    while i+n<len(s) and s[i+n]==c:
        n+=1
    r+=c+str(n)
    i+=n
print(r)
a=len(s)
b=len(r)
m=-1
z=""
i=0
while i<len(s):
    c=s[i]
    n=1
    while i+n<len(s) and s[i+n]==c:
        n+=1
    e=n-(1+len(str(n)))
    if e>m or(e==m and c==z):
        e=m
        z=c
    i+=n
print(a)
print(b)
print(z)
