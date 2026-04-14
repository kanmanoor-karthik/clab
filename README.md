💬 LAN Chat Application (Python)

👋 Hey there!

This is a simple terminal-based messaging system built using Python.
Anyone can host a server and multiple users can join and chat in real-time over the same network.

---

📁 Project Files

1. serverNEW.py 🖥️
   Hosts the chat server

2. client.py 💻
   Connects users to the server

---

⚙️ Requirements

Make sure your system has:

✅ Python 3

Check:

python3 --version

If not installed:

sudo apt update
sudo apt install python3 -y

---

✅ Git (to download project)

if ! command -v git >/dev/null 2>&1; then
  echo "Installing git..."
  sudo apt install git -y
fi

---

🚀 Setup & Run

🔽 Step 1: Download Project

cd ~
git clone https://github.com/kanmanoor-karthik/clab.git
cd clab

---

▶️ Step 2: Run Server

python3 serverNEW.py

You should see:

Server running on 0.0.0.0:5000

---

📡 Step 3: Run Client

python3 client.py

---

🔌 Connecting to Server

🟢 Method 1 (Shortcut for CLAB users)

If you're in CLAB 301, just type:

clab

---

🔵 Method 2 (Manual – for everyone else)

1. Find server IP (on server device):

ip a

or

ifconfig

Look for:

192.168.x.x

---

2. Enter in client:

Enter server address: 192.168.x.x
Enter port: 5000

---

💬 Example Chat

[17:30] user1: hello
[17:31] user2: hi
[17:31] You: how are you?

---

👨‍💻 Contributors

- [Batman](http://github.com/kanmanoor-karthik)
- [Flashman](http://github.com/kummarirahul1980)

---

✅ That’s it — you’re ready to go!