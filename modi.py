import socket
import sys

if (len(sys.argv) > 1):
    ServerIp = sys.argv[1]
else:
    print("\nPlease run with entering server's ip address \n\n")
    exit(1)

s = socket.socket()

PORT = 8787

s.connect((ServerIp, PORT))


filetosend = input('\nPlease enter file named to stored: ')
s.send(filetosend.encode())
file = open(filetosend, "rb")

SendData = file.read(99999)

while SendData:

    print("\nMessage from server:", s.recv(1024).decode("utf-8"))

    s.send(SendData)
    SendData = file.read(99999)
    print(filetosend + " copying successful and time to stored.....\nCONGRATULATION!! THE FILE IS IN OUR STORAGE SERVICE\n")

s.close()
