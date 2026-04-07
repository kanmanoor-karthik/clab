import socket
import threading
import time
import random

HOST = '0.0.0.0'
PORT = 5000

clients = {}
usernames = set()
colors = {}
lock = threading.Lock()

# ANSI colors
COLOR_LIST = [
    "\033[91m",  # red
    "\033[92m",  # green
    "\033[93m",  # yellow
    "\033[94m",  # blue
    "\033[95m",  # magenta
    "\033[96m",  # cyan
]

RESET = "\033[0m"

def get_timestamp():
    return time.strftime("%H:%M")

def recv_line(conn):
    data = b""
    while not data.endswith(b"\n"):
        chunk = conn.recv(1024)
        if not chunk:
            return None
        data += chunk
    return data.decode().strip()

def broadcast(msg):
    with lock:
        for c in list(clients):
            try:
                c.sendall(msg.encode())
            except:
                pass

def handle_client(conn, addr):
    try:
        conn.sendall(b"Enter username:\n")

        # ---- HANDSHAKE ----
        while True:
            name = recv_line(conn)
            if name is None:
                return

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
                    colors[name] = random.choice(COLOR_LIST)

            conn.sendall(b"OK\n")
            break

        print(f"{name} connected")

        # Notify others
        join_msg = f"[{get_timestamp()}] {name} joined the chat\n"
        broadcast(join_msg)

        # ---- MESSAGE LOOP ----
        while True:
            msg = recv_line(conn)
            if msg is None:
                break

            if not msg:
                continue

            username = clients[conn]
            color = colors[username]

            formatted = f"[{get_timestamp()}] {color}{username}{RESET}: {msg}\n"

            print(formatted.strip())

            # 🔥 broadcast to ALL (including sender now)
            broadcast(formatted)

    finally:
        with lock:
            if conn in clients:
                username = clients[conn]
                usernames.remove(username)
                del clients[conn]
                del colors[username]

                leave_msg = f"[{get_timestamp()}] {username} left the chat\n"
                broadcast(leave_msg)

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
