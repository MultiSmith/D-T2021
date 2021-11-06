# MAIN TASKS
# TASK №1
def filter_list(list1):
    list2 = []
    for a in list1:
        if type(a) != str:
            list2.append(a)
    return list2

# TASK №2
def first_non_repeating_letter(string1):
    string2 = []
    for a in string1:
        string2.append(a.lower())
    for a in string1:
        if string2.count(a.lower()) == 1:
            return a
    return ""

# TASK №3
def digital_root(number):
    str_num = str(number)
    while len(str_num) > 1:
        result = 0
        for i in range(len(str_num)):
            result += int(str_num[i])
        str_num = str(result)
    return result

# TASK №4
def count_pairs_of_sums(array, target):
    counter = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if (array[i] + array[j] == target):
                counter += 1
    return counter

# TASK №5
def meeting(s):
    sorted_by_name = sorted(list(map(lambda f_l: ":".join(f_l.split(":")[::-1]), s.split(";"))))
    return "(" + ")(".join(list(map(lambda s_b_n: ", ".join(s_b_n.split(":")), sorted_by_name))).upper() + ")"

# EXTRA TASKS
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

# TASK №2
def number_into_IPv4(num):
    ip1 = str(int(num / 16777216) % 256)
    ip2 = str(int(num / 65536) % 256)
    ip3 = str(int(num / 256) % 256)
    ip4 = str(int(num) % 256)
    return ".".join([ip1, ip2, ip3, ip4])