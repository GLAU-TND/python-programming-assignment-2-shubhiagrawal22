from itertools import permutations
l = list(map(str,input().split()))
m = int(max("".join(i) for i in permutations(str(i) for i in l)))
print("the largest no. possibe: " + str(m))
