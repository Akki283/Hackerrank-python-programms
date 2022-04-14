# Given an integer,N , print the following values for each integer N from 1 to N:
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary

def print_formatted(number):

    l1 = len(bin(number)[2:])

    for i in range(1, number + 1):
        print(str(i).rjust(l1, ' '), end=" ")
        print(oct(i)[2:].rjust(l1, ' '), end=" ")
        print(((hex(i)[2:]).upper()).rjust(l1, ' '), end=" ")
        print(bin(i)[2:].rjust(l1, ' '), end=" ")
        print("")
print_formatted(17)