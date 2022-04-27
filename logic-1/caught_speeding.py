def caught_speeding(speed, is_birthday):
    if speed <= 60 and not is_birthday:
        return 0
    elif 61 <= speed <= 80 and not is_birthday:
        return 1
    elif speed >= 81 and not is_birthday:
        return 2
    elif is_birthday and speed <= 65:
        return 0
    elif is_birthday and 66 <= speed <=85:
        return 1
    elif is_birthday and speed >= 86:
        return 2

print(caught_speeding(60, False))
print(caught_speeding(65, False))
print(caught_speeding(65, True))