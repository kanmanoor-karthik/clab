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

🚀 Setup & Run (Simplified)

🔽 Step 1: Download Project

cd ~
git clone https://github.com/kanmanoor-karthik/clab.git
cd clab

---

▶️ Step 2: Run Server

python3 serverNEW.py

You should see:

Server running on 0.0.0.0:5000

👉 Default port is 5000 (same for everyone unless changed in code)

---

📡 Step 3: Run Client

python3 client.py

---

🔌 Connecting to Server

You have 2 ways:

---

🟢 Method 1 (Shortcut for CLAB users)

If you're in CLAB 301, just type:

clab

It will auto-connect using preconfigured IP.

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

⚠️ Important Notes

- Both devices must be on the same WiFi network 🌐

- Do NOT use:
  
  192.168.x.255 ❌ (broadcast address)

- Use actual IP:
  
  192.168.x.x ✅

- Port is 5000 by default
  👉 It will stay same unless changed in "serverNEW.py"

---

💬 Example Chat

[17:30] user1: hello
[17:31] user2: hi
[17:31] You: how are you?

---

🔧 Troubleshooting

❌ Not connecting?

- Check server is running
- Check correct IP
- Ensure same network

---

❌ Weird output?

- Make sure latest "client.py" is used
- Restart program

---

❌ IP not working?

- Your IP may change → recheck using "ip a"

---

👨‍💻 Contributors

- "Batman" (http://github.com/kanmanoor-karthik)
- "Flashman" (http://github.com/kummarirahul1980)

---

🎯 Summary

- Clone repo
- Run server
- Run client
- Enter IP + port (5000)
- Start chatting 💬

---

✅ That’s it — you’re ready to go!