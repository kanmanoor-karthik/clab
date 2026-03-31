import socket
import threading

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
    host = input("Enter server address: ")
    port = int(input("Enter port: "))

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

    print("Connected. Start chatting...\n")

    # ---- RECEIVE THREAD ----
    threading.Thread(target=receive, args=(s,), daemon=True).start()

    # ---- SEND LOOP ----
    while True:
        try:
            msg = input(">> ")
            if msg.lower() == "exit":
                break
            s.sendall((msg + "\n").encode())
        except KeyboardInterrupt:
            break

    s.close()

if __name__ == "__main__":
    main()