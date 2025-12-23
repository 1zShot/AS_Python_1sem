def word_count(txt, separator=' '):
    w = txt.split(separator)
    res = {}
    for word in w:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res
def filter_numbers(nums, exclude_multiples_of=2):
    result = []
    for n in nums:
        if n % exclude_multiples_of != 0:
            result.append(n)
    return result
def merge_and_sort_keys(*dicts):
    merged = {}
    for d in dicts:
        for k, v in d.items():
            if k in merged:
                if v > merged[k]:
                    merged[k] = v
            else:
                merged[k] = v
    sorted_keys = sorted(merged.keys(), key=lambda x: merged[x], reverse=True)
    return sorted_keys
def sum_non_negative(*args):
    s = 0
    for num in args:
        if num >= 0:
            s += num
    return s
print("а)")
r1 = word_count('один два один')
print(r1)
r2 = word_count('red,green,blue,red', separator=',')
print(r2)

print("\nб)")
r3 = filter_numbers([1, 2, 3, 4, 5])
print(r3)
r4 = filter_numbers([10, 15, 20, 25], exclude_multiples_of=5)
print(r4)

print("\nв)")
r5 = merge_and_sort_keys({'a': 2, 'b': 3}, {'a': 5, 'c': 1})
print(r5)
r6 = merge_and_sort_keys({'x': 10}, {'y': 5}, {'z': 15})
print(r6)

print("\nг)")
r7 = sum_non_negative(1, -2, 3, -4, 5)
print(r7)
r8 = sum_non_negative(-10, -20)
print(r8)
