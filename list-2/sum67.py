def sum67(nums):
    count = 0
    blocked = False
  
    for n in nums:
        if n == 6:
            blocked = True
            continue
        if n == 7 and blocked:
            blocked = False
            continue
        if not blocked:  
            count += n
    return count

print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))