def xyz_there(str):
    i=0
    while "xyz" in str[i:]:
        if str[i-1+str[i:].index("xyz")] != ".":
            return True
        i += str[i:].index("xyz")+2
    return False

print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))