def CheckIsPowerOf2(n):
    result = 1
    for i in range(31):
        if result > n:
            break
        if result == n:
            return True
        result = result << 1
    return False


print(CheckIsPowerOf2(1))