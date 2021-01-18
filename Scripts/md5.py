import string
import hashlib

x = "cb7a53dd721f4ca90b8fd3dbdabeda5a"
chars = list(string.ascii_lowercase + string.digits)

for i in chars:
    for j in chars:
        for k in chars:
            for a in chars:
                for b in chars:
                    m = hashlib.md5()
                    m.update("shaktictf{" + i+j+k+a+b + "}")
                    if m.hexdigest() == x:
                        print "shaktictf{" + i+j+k+a+b + "}"
                        break
