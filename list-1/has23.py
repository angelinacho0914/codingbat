def has23(nums):
    for i in nums:
        if i == 2 or i == 3:
            return True
    return False

print(has23([2, 5]))
print(has23([4, 3]))
print(has23([4, 5]))