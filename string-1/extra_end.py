def extra_end(str):
    return f'{str[-2:]}{str[-2:]}{str[-2:]}'

print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))