#You are given a string S and width w.
#Your task is to wrap the string into a paragraph of width .

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
############## alternate logic ######################
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = 4
print(a[0],end='')
for i in range(1,len(a)):

    print(a[i],end='')
    if i%b == 0:
        if i == 0:
            continue
        print()
