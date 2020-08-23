def NextGreaterElements(nums):
    if not nums:
        return []
    stack = []
    res = [-1 for i in range(len(nums))]
    for i in range(len(nums)):
        if stack and nums[i] > nums[stack[-1]]:
            while stack and nums[i] > nums[stack[-1]]:
                pop_index = stack.pop()
                res[pop_index] = nums[i]
        stack.append(i)
    for i in range(len(nums)):
        if stack and nums[i] > nums[stack[-1]]:
            while stack and nums[i] > nums[stack[-1]]:
                while stack and nums[i] > nums[stack[-1]]:
                    pop_index = stack.pop()
                    res[pop_index] = nums[i]
        stack.append(i)
        if nums[stack[0]] == nums[stack[-1]]:
            break
    return res

print(NextGreaterElements([1,3,5,9,1,2,6]))