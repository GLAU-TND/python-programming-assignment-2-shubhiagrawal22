def consecutive(a):
    c = 0
    while(a!=0):
        a = (a & (a << 1))
        c+=1
    return c
print(consecutive(int(input())))
