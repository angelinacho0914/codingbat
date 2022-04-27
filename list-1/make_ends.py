def make_ends(nums):
    l = []
    l.append(nums[0])
    l.append(nums[-1])
    return l

print(make_ends([1, 2, 3]))
print(make_ends([1, 2, 3, 4]))
print(make_ends([7, 4, 6, 2]))