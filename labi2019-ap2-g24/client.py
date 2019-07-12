import time 
import datetime
import sys
import random
import json
import csv
import requests
from socket import *
 #função que valida os argumentos
def valid():
	if len(sys.argv)<4:
		print("ERRO -> Deve chamar o programa com: python3 client.py interval num [country or id]")
		sys.exit(0)
	if not sys.argv[1].isdigit():
		print("ERRO -> O primeiro argumento deve ser um valor inteiro")
		sys.exit(0)
	if not sys.argv[2].isdigit() :
		print("ERRO -> O segundo argumento deve ser um valor inteiro")
		sys.exit(0)
	if not (sys.argv[3].isdigit() or sys.argv[3].isalpha()):
		print("ERRO -> O terceiro argumento deve ser um valor inteiro ou um nome")
		sys.exit(0)
#função que abre o ficheiro json e se o 3º argumento for um texto guarda-o num array e vai escolher
#um random, se o argumento 3 for numérico procura o id no ficheiro Se esse país ou id não estiverem 
# no ficheiro dá erro e sai do programa
def host(): 
	countries = []
	if sys.argv[3].isalpha() :
		servers = open("servers.json","r")
		servers = json.load(servers)
		for server in servers ['servers'] :
			if sys.argv[3] == server['country'] :
				countries.append(server['host'])
		
		if len(countries) <= 0 :
			print ("ERRO->País inexistente")
			sys.exit(0)
		else:
			r = countries[random.randint(0,len(countries)-1)] 
			r = r.split(':')
			return r

	if sys.argv[3].isdigit():
		servers = open("servers.json","r")
		servers = json.load(servers)
		for server in servers['servers'] :
			if int(sys.argv[3]) == server['id']:
				c = server['host'].split(':')
				return c
			else:
				print("ERRO->id inexistente")
				sys.exit(0)
#função faz a ligação com o servidor e calcula o download se não for possível conectar com
# o servidor tenta reconectar novamente 
def download(servip,servport):

	tcp_s = socket(AF_INET,SOCK_STREAM)
	svaddr = (servip,int(servport))
	try:
		tcp_s.connect(svaddr)
	except error:
		return 0
	tempoantes = time.time()
	buffer = 0
	tamanhoDownload = random.randint(10,100)
	while 1:
		tempodepois = time.time()
		if (tempodepois-tempoantes) > 10:
			tempodepois = time.time()
			break
		if buffer >= tamanhoDownload*1000000:
			tempodepois = time.time()
			break
		tcp_s.send(('DOWNLOAD ' +str(tamanhoDownload*1000000) + '\n').encode('utf-8'))
		resp = tcp_s.recv(8192)
		buffer += len(resp)
	
	return ((buffer/1000000)/(tempodepois-tempoantes))
#função faz a ligação com o servidor e calcula a latência se não for possível conectar 
# com o servidor tenta reconectar novamente 	   
def	ping(servip,servport):		
	tcp_s = socket(AF_INET,SOCK_STREAM)
	svaddr = (servip,int(servport))
	try:
		tcp_s.connect(svaddr)
	except error:
		return -1
	tempoantes = (time.time())*1000

	tcp_s.send(('PING ' + str(time.time()*1000) + '\n').encode('utf-8'))
	resp = tcp_s.recv(2048)
	tcp_s.close()
	tempo = ((time.time())*1000 - tempoantes)
	return tempo
#função que abre o ficheiro e retorna o id do host dado 
def read_json(server):
	servers = open("servers.json","r")
	servers = json.load(servers)
	for x in servers['servers'] :
		if x['host'] == server:
			return x['id'] 

#função que escreve no ficheiro csv e tem a lógica prncipal do programa
def main():
	with open('report.csv', mode='w') as csv_file:
		fieldnames = ['contador', 'id', 'data', 'latencia', 'largura de banda', 'check']

		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()

		nTestes = 0
		valid()
		while(nTestes < int(sys.argv[2])):
			server = host()
			downloadAtual = download(server[0], int(server[1]))
			print("Download -> " + str(downloadAtual) +" MB")
			pingAtual = ping(server[0],int(server[1]))
			print("Ping -> " + str(pingAtual) + " ms")
			nTestes += 1
			time.sleep(int(sys.argv[1]))
			testesRestantes = int(sys.argv[2])-nTestes
			print("Teste realizado com sucesso, faltam %d para terminar\n" %testesRestantes)
			writer.writerow({'contador': str(nTestes) , 'id': str(read_json(server[0] + ':' + server[1])), 'data': str(datetime.datetime.now().isoformat()), 'latencia': str(pingAtual), 'largura de banda': str(downloadAtual), 'check': str(nTestes) + str(read_json(server[0] + ':' + server[1])) + str(datetime.datetime.now().isoformat()) + str(pingAtual) + str(downloadAtual) })
	
main()






