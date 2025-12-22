n=int(input("Введите число n: "))
kv={a: a**2 for a in range(1, n + 1)}
print(f"квадраты: {kv}")

sp=[{1: 2}, {3: 4}, {5: 6}]
print(f"список словарей: {sp}")
sz=[]
for s in sp:
    for z in s.values():
        sz.append(z)
print(f"список знач: {sz}")


i={1:'',2:'abc',3:None,4:0,5:'xyz'}

print(f"исходный словарь: {i}")
o={}
for k, z in i.items():
    if z:
        o[k]=z
print(f"чистый словарь{o}")
