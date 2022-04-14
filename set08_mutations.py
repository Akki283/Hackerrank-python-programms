# The first line contains the number of elements in set A.
# The second line contains the space separated list of elements in set A.
# The third line contains integer N, the number of other sets.
# The next 2*N lines are divided into N parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.





n = int(input())
a = set(map(int, input().split()))
m = int(input())
for i in range(m):
    operation = input().split()
    if operation[0] == 'intersection_update':
        new_set = set(map(int, input().split()))
        a.intersection_update(new_set)
    elif operation[0] == 'update':
        new_set = set(map(int, input().split()))
        a.update(new_set)
    elif operation[0] == 'symmetric_difference_update':
        new_set = set(map(int, input().split()))
        a.symmetric_difference_update(new_set)
    elif operation[0] == 'difference_update':
        new_set = set(map(int, input().split()))
        a.difference_update(new_set)
    else:
        pass
print(sum(a))