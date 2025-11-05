# Задание №6
def print_positive_n(A, B, H):
    if A>=B:
        print("A должно быть меньше B")
        return
    for n in range(A, B, H):
        if n>0:
            print(n)
A=-5
B=10
H=2
print_positive_n(A, B, H)
