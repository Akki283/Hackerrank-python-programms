#The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English,
# some have subscribed to only French and some have subscribed to both newspapers.
#You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the
# French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to both
# the newspapaer






n = int(input())
a = set(map(int,input().split()))
m = int(input())
b = set(map(int,input().split()))
c = a.intersection(b)
output = len(c)
print(output)