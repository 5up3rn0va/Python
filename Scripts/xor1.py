str = "label"
flag = ""

for i in str:
    flag += chr(ord(i) ^ 13)

print(flag)