# TASK №3
def digital_root(number):
    str_num = str(number)
    while len(str_num) > 1:
        result = 0
        for i in range(len(str_num)):
            result += int(str_num[i])
        str_num = str(result)
    return result

# TESTS
print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))