# TASK №2
def first_non_repeating_letter(string1):
    string2 = []
    for a in string1:
        string2.append(a.lower())
    for a in string1:
        if string2.count(a.lower()) == 1:
            return a
    return ""

# TESTS
print(first_non_repeating_letter("stress"))
print(first_non_repeating_letter("sTreSS"))
print(first_non_repeating_letter(""))
print(first_non_repeating_letter("ssss"))