def end_other(a, b):
    if len(a) >= len(b):
        longer = a
        shorter = b
    else:
        longer = b
        shorter = a
    return longer.lower().endswith(shorter.lower())

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))