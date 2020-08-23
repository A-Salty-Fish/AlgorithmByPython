def aplusb(a, b):
    while b != 0:
        # b = (a & b) << 1
        # a = (a ^ b) & 0xffffffff
        a, b = (a ^ b) & 0xffffffff, (a & b) << 1
        # a = (a ^ b) & 0xffffffff
        # b = (a & b) << 1
    return a

print(aplusb(13,4))
