# TASK №2
def number_into_IPv4(num):
    ip1 = str(int(num / 16777216) % 256)
    ip2 = str(int(num / 65536) % 256)
    ip3 = str(int(num / 256) % 256)
    ip4 = str(int(num) % 256)
    return ".".join([ip1, ip2, ip3, ip4])

# TESTS
print(number_into_IPv4(2149583361))
print(number_into_IPv4(32))
print(number_into_IPv4(0))
