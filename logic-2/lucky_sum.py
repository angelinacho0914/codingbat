def lucky_sum(a, b, c):
    sum = 0
    list = [a,b,c,13]
    for n in list[:list.index(13)]:
        sum += n
    return sum

print(lucky_sum(1, 2, 3))
print(lucky_sum(1, 2, 13))
print(lucky_sum(1, 13, 3))