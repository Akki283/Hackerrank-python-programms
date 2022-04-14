# set: concept of the symmetric diffrence



M = int(input())
m=set(map(int,input().split()))
N = int(input())
n = set(map(int,input().split()))

mdif = m.symmetric_difference(n)
ndif = n.symmetric_difference(m)

a = mdif.union(ndif)
b = list(a)
b.sort()
for i in b:
    print(i)