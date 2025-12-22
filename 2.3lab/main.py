def SumMtr(m1, m2):
    r=[]
    for i in range(len(m1)):
        s=[]
        for j in range(len(m1[0])):
            s.append(m1[i][j] + m2[i][j])
        r.append(s)
    return r

a=[[1,2,3],[4,5,6]]
b=[[10,20,30],[40,50,60]]
c=SumMtr(a,b)
print(c)
