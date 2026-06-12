import socket
import threading

SERVER_IP = "172.19.152.101"
PORT = 5000

def recieve_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("\nPeer disconnected.")
                break
            print(f"\nPeer: {data.decode()}")
            print("You:",end="",flush=True)
        except:
            break

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    client.connect((SERVER_IP,PORT))

    threading.Thread(target=recieve_messages,args=(client,),daemon=True).start()
    while True:
        msg = input("Message: ")
        if msg.lower() == "quit":
            break
        client.sendall(msg.encode())
