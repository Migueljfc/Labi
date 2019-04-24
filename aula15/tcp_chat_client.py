import socket, select, sys

TCP_PORT = int(sys.argv[1])

def main(argv):
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tcp_client.bind(("127.0.0.1",0))
    server_addr = ("127.0.0.1",1234)
    
    tcp_client.connect(server_addr)
    while 1:
        rsocks = select.select([tcp_client,sys.stdin,],[],[])[0]
        for sock in rsocks:
            if sock == tcp_client:
                b_data = tcp_client.recv(4096)
                str_data = b_data.decode("utf-8")
                sys.stdout.write("Message (form server) %s \n" % str_data)

            elif sock == sys.stdin:
                str_data = sys.stdin.readline()
                b_data = str_data.encode("utf-8")
                tcp_client.send(b_data)
    tcp_client.close()
main(argv)