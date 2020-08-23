def SingleNumber(A):
    ans = 0
    for x in A:
        ans = ans ^ x
    return ans


print(SingleNumber([1,1,3,3,4]))