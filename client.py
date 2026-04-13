import socket
import threading
import sys
import readline
import datetime

def receive(s):
    while True:
        try:
            data = s.recv(1024)
            if not data:
                break

            msg = data.decode()

            # get current typed input
            current = readline.get_line_buffer()

            # clear current line
            sys.stdout.write("\r")
            sys.stdout.write(" " * (len(current) + 10))
            sys.stdout.write("\r")

            # print message cleanly
            print(msg, end="")

            # redraw input
            sys.stdout.write("You: " + current)
            sys.stdout.flush()

        except:
            break


def main():
    hostx = input("Enter server address: ")

    if hostx == "clab":
        host = "10.4.3.142"
        port = 5000
    else:
        host = hostx
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
        print("Username taken. Restart (Ctrl+C) and try again.")

    print("Connected. Start chatting...\n")

    # ---- RECEIVE THREAD ----
    threading.Thread(target=receive, args=(s,), daemon=True).start()

    # ---- SEND LOOP ----
    while True:
        try:
            msg = input("You: ")
            if msg.lower() == "exit":
                break
            s.sendall((msg + "\n").encode())
        except KeyboardInterrupt:
            break

    s.close()


if __name__ == "__main__":
    main()