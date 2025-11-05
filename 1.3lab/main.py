import math
def calculate_sum(n):
    if n<=0:
        print("n должно быть натуральным числом")
        return None
    ts=0
    for i in range(1, n+1):
        ts+=((-1)**(i + 1))*math.cos(i)
    return ts
n=5
r=calculate_sum(n)
print(r)
