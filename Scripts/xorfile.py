def xor(data, key):
    l = len(key)
    return bytearray((
        (data[i] ^ key[i % l]) for i in range(0,len(data))
    ))

data = bytearray(open('cipher.jpg', 'rb').read())

key = bytearray([0x77,0x30,0x6d,0x33,0x6e,0x5f,0x70,0x30,0x77,0x33,0x72])
a = xor(data, key)
newFile = open("1.jpg", "wb")
newFile.write(a)
