# The first line contains integer n, the number of elements in the set m.
# The second line contains s space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer N , the number of commands.
# The next  lines contains either pop, remove and/or discard commands followed by their associated value.





n= int(input())
s = set(map(int,input().split()))
m = int(input())

for i in range(m):
    entry = input().split()
    if entry[0]=='remove':
        s.remove(int(entry[1]))
    elif entry[0] =='discard':
        s.discard(int(entry[1]))
    else:
        s.pop()

print(sum(s))