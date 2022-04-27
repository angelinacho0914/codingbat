def sorta_sum(a, b):
    sum_num = a + b
    if 10 <= sum_num <= 19:
        return 20
    return sum_num

print(sorta_sum(3, 4))
print(sorta_sum(9, 4))
print(sorta_sum(10, 11))