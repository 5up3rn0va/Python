from pwn import * # pip install pwntools
import json
from base64 import b64decode
import codecs
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

for i in range(100):
	received = json_recv()

	print("Received type: ")
	print(received["type"])
	print("Received encoded value: ")
	print(received["encoded"])

	encoding = received["type"]
	encoded = received["encoded"]

	if encoding == "base64":
		decoded = b64decode(encoded).decode() 
	elif encoding == "hex":
		decoded = bytes.fromhex(encoded).decode()
	elif encoding == "rot13":
		decoded = codecs.encode(encoded, 'rot_13')
	elif encoding == "bigint":
		decoded = long_to_bytes(int(encoded, 16)).decode()
	elif encoding == "utf-8":
		decoded = ''.join(chr(b) for b in encoded)

	to_send = {
    	"decoded": decoded
	}
	
	json_send(to_send)

json_recv()
