import math
def TriangleP(a, h):
    a2=a/2
    bs= math.sqrt(h**2+a2**2)
    p=a+2*a2
    return p
print("=" * 50)
print("периметр рб")
print("=" * 50)
a= float(input("основание: "))
h= float(input("высота: "))
if a <= 0 or h <= 0:
    print("ошибка")
else:
    r= TriangleP(a, h)
    print(f"периметр: {r:.2f}")
