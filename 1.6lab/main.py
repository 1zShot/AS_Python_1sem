def remove_every_nth_character(s, n):
    if n<=0:
        return "n>0"
    r=''.join([char for i, char in enumerate(s) if(i+1)%n!=0])
    return r

s="abcdefghij"
n=3
r=remove_every_nth_character(s, n)
print(r)
