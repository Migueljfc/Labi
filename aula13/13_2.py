import hashlib
import sys

if len(sys.argv)<2:
    print("Deve passar o nome do ficheiro como argumento")

file_name = sys.argv[1]
h = hashlib.sha1()
f = open(file_name, "rb")
buffer = f.read(512)

while len(buffer) >0:
    h.update(buffer)
    buffer = f.read(512)
f.close()
print()
print("SHA-1 digest of " +file_name+ ":" + h.hexdigest())
print()