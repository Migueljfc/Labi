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
decipher = ARC4.new(key)
decrypted = decipher.decrypt(cryptogram)
print(decrypted.decode('utf-8'))