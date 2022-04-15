# sets : no idea solution
#there is an array of n integers. There are also  disjoint sets,A  and B, each containing M integers. You like all the integers in set A
# and dislike all the integers in set B. Your initial happiness is 0 . For each  integer in the array,n if A=N, you add 1 to your happiness.
# If B=N, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

#Note: Since A and B are sets, they have no repeated elements. However,N the array might have






a = input().split()
n = a[0]
m = a[1]

arry = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
total_happiness = 0
for item in arry:
    if item in set_a:
        total_happiness = total_happiness + 1
    elif item in set_b:
        total_happiness = total_happiness - 1
print(total_happiness)


