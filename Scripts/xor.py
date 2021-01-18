head = "88e892d36e4f3a763e757276316d336f"
sigs = ["FFD8FFDB", "FFD8FFE000104A4649460001", "FFD8FFEE"]

for i in sigs:
    key = hex(int(head[:len(i)], 16) ^ int(i, 16))[2:]
    print(bytes.fromhex(key).decode('utf-8'))