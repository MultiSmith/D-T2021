# TASK №1
def filter_list(list1):
    list2 = []
    for a in list1:
        if type(a) != str:
            list2.append(a)
    return list2

# TESTS
print(filter_list([1,2,'a','b']))
print(filter_list([1,'a','b',0,15]))
print(filter_list([1,2,'aasf','1','123',123]))