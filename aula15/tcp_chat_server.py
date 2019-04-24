import socket, select,sys

TCP_PORT = int(sys.argv[1])
TCP_CONNECTION_LIST = []
RECV_BUFFER = 4096

def brodcast_data(message):
    for sock in TCP_CONNECTION_LIST[1:]:
        msg = "via TCP -->" + message
        sock.send(msg.encode("utf-8"))

def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(("127.0.0.1", TCP_PORT))
    tcp_socket.listen(10)
    TCP_CONNECTION_LIST.append(tcp_socket)

    print("Chat server started on port tcp://:%d" % (TCP_PORT))

    while 1:
        read_sockets = select.select(TCP_CONNECTION_LIST,[],[])[0]

        for sock in read_sockets:
            if sock == tcp_socket:
                sockfd, addr = tcp_socket.accept()
                TCP_CONNECTION_LIST.append(sockfd)
                print("Client (%s, %s) connected" % addr)

                brodcast_data("[%s:%s] entered room \n" % addr)

            else:
                b_data = sock.recv(RECV_BUFFER)
                print("[Received: ]" +b_data.decode("utf-8"))
                brodcast_data(b_data.upper().decode("utf-8"))
        
       
    tcp_socket.close()
main()
