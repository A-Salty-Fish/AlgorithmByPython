def divide(dividend, divisor):
    INT_MAX = 214783647
    if divisor == 0:
        return INT_MAX
    neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
    a, b = abs(dividend), abs(divisor)
    ans, shift = 0, 31
    while shift >= 0:
        if a >= b << shift:
            a -= b << shift
            ans += 1 << shift
        shift -= 1
    if neg:
        ans = -ans
    if ans > INT_MAX:
        return INT_MAX
    return ans


print(divide(10,2))
