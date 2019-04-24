import requests
import time
tstart = time.time()
f = requests.get("http://www.ua.pt")
duration = time.time()-tstart
Vel=int(f.headers['Content-Length']) /duration/1024.0

print("Código:",f.status_code)
print("Cabeçalhos:",f.headers)

#print tempo de acesso 
print("Tempo de acesso2: %.3f segundo" % duration)

#Print velocidade KB
print("Velocidade2: %.3f KB/segundo" % Vel)

print("Tamanho1: {}" .format(f.headers['Content-Length']))
print("Tamanho2 (KB): ", float((f.headers['Content-Length'])/1024.0))
