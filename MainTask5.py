# TASK №5
def meeting(s):
    sorted_by_name = sorted(list(map(lambda f_l: ":".join(f_l.split(":")[::-1]), s.split(";"))))
    return "(" + ")(".join(list(map(lambda s_b_n: ", ".join(s_b_n.split(":")), sorted_by_name))).upper() + ")"

# TESTS
print(meeting("Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))