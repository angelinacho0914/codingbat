def sum13(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) >= 1 and 13 not in nums:
        return sum(nums)
    elif len(nums) >= 1 and 13 in nums:
        sum_num = 0
        for i in range(len(nums)):
            if nums[i] != 13:
                sum_num += nums[i]
            elif nums[i] == 13:
                i += 2
        return sum_num


print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]))