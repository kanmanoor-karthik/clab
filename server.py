import socket
import threading

HOST = '0.0.0.0'
PORT = 5000

clients = {}
usernames = set()
lock = threading.Lock()

def recv_line(conn):
    data = b""
    while not data.endswith(b"\n"):
        chunk = conn.recv(1024)
        if not chunk:
            return None
        data += chunk
    return data.decode().strip()

def broadcast(msg, sender):
    with lock:
        for c in list(clients):
            if c != sender:
                try:
                    c.sendall(msg.encode())
                except:
                    pass

def handle_client(conn, addr):
    try:
        conn.sendall(b"Enter username:\n")

        # ---- SAFE HANDSHAKE LOOP ----
        while True:
            name = recv_line(conn)
            if name is None:
                return  # client disconnected

            if not name:
                conn.sendall(b"Name required\nEnter username:\n")
                continue

            with lock:
                if name in usernames:
                    conn.sendall(b"TAKEN\nEnter username:\n")
                    continue
                else:
                    usernames.add(name)
                    clients[conn] = name

            conn.sendall(b"OK\n")
            break

        print(f"{name} connected")

        # ---- MESSAGE LOOP ----
        while True:
            msg = recv_line(conn)
            if msg is None:
                break

            if not msg:
                continue

            full = f"{clients[conn]}: {msg}\n"
            print(full.strip())
            broadcast(full, conn)

    finally:
        with lock:
            if conn in clients:
                username = clients[conn]
                usernames.remove(username)
                del clients[conn]
                print(f"{username} disconnected")

        conn.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()

    print(f"Server running on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()