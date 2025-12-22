def NOD(a, b):
    if a==0:
        return b
    else:
        return NOD(b%a,a)

print("четыре натуральных числа:")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=int(input("d="))

nod_ab=NOD(a,b)
print(f"НОД({a},{b})={nod_ab}")
nod_ac=NOD(a,c)
print(f"НОД({a},{c})={nod_ac}")
nod_ad = NOD(a,d)
print(f"НОД({a},{d})={nod_ad}")
