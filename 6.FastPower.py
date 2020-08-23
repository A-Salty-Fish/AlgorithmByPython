def fastPower(a,b,n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = result * a % b
        a = a * a % b
        n = n / 2
    return result % b


print(fastPower(2,3,31))