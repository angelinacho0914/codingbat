def max_end3(nums):
    l = []
    max_num = max(nums)
    for i in range(len(nums)):
        l.append(max_num)
    return l

print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([2, 11, 3]))