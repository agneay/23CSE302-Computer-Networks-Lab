import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

def recieve_message(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print("\n Peer disconnected.")
                break
            print(f"\nPeer: {data.decode()}")
            print("You:", end="",flush=True)
        except:
            break

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as server:
    server.bind((HOST,PORT))
    server.listen(1)

    print(f"Server listening on port {PORT}..")
    conn, addr = server.accept()
    print(f"Connected to {addr}")

    threading.Thread(target=recieve_message,args=(conn,),daemon=True).start()

    while True:
        msg = input("You : ")
        if msg.lower() == "quit":
            break
        conn.sendall(msg.encode())

    conn.close()
