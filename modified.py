import socket

s = socket.socket()

host_name = socket.gethostname()
IPADDRESS = socket.gethostbyname(host_name)

PORT = 8787
print("Server's ip address: ", IPADDRESS)
print("Listening to the port: ", PORT)
print("--------------------------------------")
print("Connection in progress........")

s.bind(('', PORT))

s.listen(10)

while True:

    conn, addr = s.accept()

    msg =  "\n\nHello Dear, [IP address: "+ addr[0] + "], \nWelcome to our services. \nDon't worry.. Your file is being secured.\n-Server-\n"
    conn.send(msg.encode())

    filename = conn.recv(1024).decode("utf-8")
    file = open(filename, "wb")

    RecvData = conn.recv(99999)

    while RecvData:
        file.write(RecvData)
        RecvData = conn.recv(99999)

    file.close()
    print("\nCopying sucessful..... \n")

    conn.close()
    print("Thank you for using our service. BYE!!! \n")

    break
