import heapq


def MergeNumber(nubers):
    Q = []
    ans = 0
    for i in nubers:
        heapq.heappush(Q, i)
    while len(Q) > 1:
        a = heapq.heappop(Q)
        b = heapq.heappop(Q)
        ans = ans + a + b
        heapq.heappush(Q, a + b)
    return ans


print(MergeNumber([1, 2, 3, 4, 5, 6]))
