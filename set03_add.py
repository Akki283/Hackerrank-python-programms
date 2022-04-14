# set: add() to get only the unique elements
#Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection.
# She asked for your help. You pick the stamps one by one from a stack of  country stamps.

n = int(input())
countries = set()

for i in range(n):
    # countries.add(input())
    a = input()
    countries.add(a)

print(len(countries))