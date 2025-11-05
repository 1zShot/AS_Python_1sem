def product_maxelem(lst):
    if not lst:
        return None
    max_v=max(lst)
    max_i=lst.i(max_v)
    rightelem=lst[max_i+1:]
    prod=1
    for elem in rightelem:
        prod*=elem
    return prod if rightelem else None

lst=[3, 5, 2, 7, 4, 8, 1]
r=product_maxelem(lst)
print(r)
