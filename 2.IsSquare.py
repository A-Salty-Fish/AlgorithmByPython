def isPerfectSquare(num):
    left = 0
    right = num
    while right - left > 1:
        mid = (left + right) / 2
        if mid * mid <= num:
            left = mid
        else:
            right = mid

    result = 0
    if left * left < num:
        result = right
    else:
        result = left
    return result * result == num


print(isPerfectSquare(15))
