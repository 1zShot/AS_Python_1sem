def delete_char(txt, ch):
    res = ""
    for c in txt:
        if c != ch:
            res += c
    return res
def replace_char(txt, old_ch, new_ch):
    res = ""
    for c in txt:
        if c == old_ch:
            res += new_ch
        else:
            res += c
    return res
def count_char(txt, ch):
    cnt = 0
    for c in txt:
        if c == ch:
            cnt += 1
    return cnt

s = "Авраменко"
r1 = delete_char(s, 'а')
print(r1)
r2 = replace_char(s, 'е', 'Е')
print(r2)
r3 = count_char(s, 'н')
print(r3)
print()
s2 = "Авраменко Александр Дмитриевич"
r4 = delete_char(s2, ' ')
print(r4)
r5 = replace_char(s2, 'а', 'А')
print(r5)
r6 = count_char(s2, 'р')
print(r6)
