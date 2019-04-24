import os 
import sys
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA

if len(sys.argv)<3:
    print("Usage: python3 "+sys.argv[0]+" file_to_encrypt key")
    quit()
fname = sys.argv[1]
if len(sys.argv[2])<5:
    h=SHA.new()
    h.update(sys.argv[2].encode('utf-8'))
    key=h.hexdigest()
else:
    key = sys.argv[2] [0:256]

cipher = ARC4.new( key )
f = open( fname ,"rb")
for line in f:
    cryptogram = cipher.encrypt(line)
    os.write(1,cryptogram)
f.close()
 
