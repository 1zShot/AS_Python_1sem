def product_of_elements_right_of_max(lst):
    if not lst:
        return None
    max_value = max(lst)
    max_index = lst.index(max_value)
    right_elements=lst[max_index+1:]
    prod=1
    for element in right_elements:
        prod*=element
    return prod if right_elements else None

lst=[3, 5, 2, 7, 4, 8, 1]
r=product_of_elements_right_of_max(lst)
print(r)
