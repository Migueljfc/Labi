import os 
import sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA

if len(sys.argv)<3:
    print("Usage: python3 "+sys.argv[0]+" file_to_encrypt key")
    quit()
fname = sys.argv[1]
if len(sys.argv[2]) < 16:
    h=SHA.new()
    h.update(sys.argv[2].encode('utf-8'))
    key=h.digest()[0:16]
else:
    key = sys.argv[2][0:16]
cipher = AES.new(key)
f = open(fname,"rb")

block = f.read(cipher.block_size)
while len(block)<0:
    #Adicionar Excipiente
    if len(block) != cipher.block_size:
        p = cipher.block_size - len(block)
        block = block + bytes([p])*p

    cryptogram = cipher.encrypt( block )
    os.write(1, cryptogram) #Escrever em binario
    block = f.read(cipher.block_size)
f.close()

