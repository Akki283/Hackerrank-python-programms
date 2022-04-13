#the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.

string = 'ABCDCDC'
sub_string = 'CDC'
count =0
a =len(string)
b = len(sub_string)
for i in range (a-b+1):
    if (string[i:(b+i)] == sub_string):
        count = count + 1
print(count)
