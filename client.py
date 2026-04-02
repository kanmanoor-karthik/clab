import socket
import threading


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
def receive(s):
    while True:
        try:
            data = s.recv(1024)
            if not data:
                break
            print("\r" + data.decode() + ">> ", end="")
        except:
            break

def main():
    hostx= input("Enter server address: ")
    host = None
    if hostx == "clab" : 
        host = "10.4.3.142"
        port=5000
    else :
        host = hostx
        port = int(input("Enter port: "))
    if  not host and port:
        print("Please fill up the host and port")
        return
    else :
        pass
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect((host, port))
    
    # ---- USERNAME HANDSHAKE ----
    while True:
        prompt = s.recv(1024).decode()
        print(prompt, end="")

        name = input().strip()
        if not name:
            print("Name is required...")
            continue

        s.sendall((name + "\n").encode())

        response = s.recv(1024).decode()
        if "OK" in response:
            break
        print(response)
        print("username has been taken try restarting the file by clicking ctrl+c and reopen")

    print("Connected. Start chatting...\n")

    # ---- RECEIVE THREAD ----
    threading.Thread(target=receive, args=(s,), daemon=True).start()

    # ---- SEND LOOP ----
    while True:
        try:
            msg = input(">> ")
            if msg.lower() == "exit":
                break
            s.sendall(( msg + "\n").encode())
        except KeyboardInterrupt:
            break

    s.close()

if __name__ == "__main__":
    main()