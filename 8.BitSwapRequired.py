def bitSwapRequired(a, b):
    c = a ^ b
    result = 0
    for i in range(32):
        if c & (1 << i) != 0:
            result += 1
    return result


print(bitSwapRequired(31, 1))
