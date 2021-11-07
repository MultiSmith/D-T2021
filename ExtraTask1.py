# TASK №1
def nextBigger(num):
    arr = list(str(num))
    max_n = int("".join(sorted(arr, reverse=True)))
    min_n = sorted(arr)
    while num <= max_n:
        num += 1
        if sorted(list(str(num))) == min_n:
            return num
    return -1

# TESTS
print(nextBigger(12))
print(nextBigger(513))
print(nextBigger(2017))