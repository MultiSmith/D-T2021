# TASK №4
def count_pairs_of_sums(array, target):
    counter = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if (array[i] + array[j] == target):
                counter += 1
    return counter

# TESTS
print(count_pairs_of_sums([1, 3, 6, 2, 2, 0, 4, 5], 5))
print(count_pairs_of_sums([-1, 0, -2, 3, 6, 4], 4))
print(count_pairs_of_sums([4, 7, 1], 3))