l = list(map(str,input().split()))
c = [l[0]]
for i in range(len(l)):
    for j in range(0,len(l)):
        if c[i][-1]==l[j][0]:
            c.append(l[j])
            l.remove(l[j])
            l.insert(j,"0")
            break
print(c)
