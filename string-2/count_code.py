def count_code(str):
    return str.count('code') + str.count('cope') + str.count('cooe') + str.count('coze')

print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))