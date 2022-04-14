# using set to find the average of the plants with distinct heights:


def average(array):
    a = set(array)
    n = len(a)
    avg = sum(a) / n
    return format(avg, '.3f')


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)