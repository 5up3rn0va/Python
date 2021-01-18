from itertools import cycle
import string

def xor(msg, key):
    return bytes([_a ^ _b for _a, _b in zip(msg, cycle(key))])

with open("cipher.txt", 'rb') as f:
  cipher = f.read()

prefix = b"Message : shaktictf{"
suffix = b"}:e.o.m"
a = cipher[:len(prefix)]
b = cipher[-len(suffix):]

chars = [xor(cipher[20:21], i.encode()) for i in string.printable]

for c in chars:
	key = xor(a, prefix) + c + xor(b, suffix)
	print(xor(cipher,key))
