def filter_and_sort(lst):
    fn=[num for num in lst if num>10]
    sn=sorted(fn)
    return sn

lst=[5, 12, 3, 18, 7, 21, 10]
r=filter_and_sort(lst)
print(r)
