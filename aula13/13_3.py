from Crypto.Hash import SHA256
import sys

if len(sys.argv)<2:
    print("Deve passar o nome do ficheiro como argumento")
    quit()

file_name = sys.argv[1]
h = SHA256.new()
f = open(file_name, "rb")

for line in f:
    h.update(line)
    
f.close()

print()
print(h.hexdigest())
print()