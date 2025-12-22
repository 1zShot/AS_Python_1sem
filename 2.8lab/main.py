a="failik.txt"
c=0
with open(a, 'r') as a:
    z=a.read().split()
    for t in z:
        x=int(t)   
        if x%2==0:
            c+=1
print(f"четные числа: {c}")
