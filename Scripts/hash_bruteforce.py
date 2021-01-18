import string
import hashlib

x = "bd737ce0d884c0dd54adf35fdb794b60"
chars = list(string.ascii_lowercase)

for i in chars:
    for j in chars:
        for k in chars:
            for a in chars:
                for b in chars:
                    m = hashlib.md5()
                    m.update("mmal7" + i+j+k+a+b)
                    if m.hexdigest() == x:
                        print "0xL4ugh{1_" + i+j+k+a+b + "}"
                        break