def SingleNumberIV(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == nums[mid - 1]:
            if (mid - left + 1) % 2 == 1:
                right = mid - 2
            else:
                left = mid + 1
        elif nums[mid] == nums[mid + 1]:
            if (right - mid + 1) % 2 == 1:
                left = mid + 2
            else:
                right = mid - 1
        else:
            return nums[mid]
    return nums[left]


print(SingleNumberIV([1,1,2,2,3,3,4,5,5,6,6]))