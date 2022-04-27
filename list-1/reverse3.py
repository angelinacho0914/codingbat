def reverse3(nums):
    l = []
    for i in range(len(nums)-1, 0, -1):
        l.append(nums[i])
    l.append(nums[0])
    return l


print(reverse3([1, 2, 3]))
print(reverse3([5, 11, 9]))
print(reverse3([7, 0, 0]))